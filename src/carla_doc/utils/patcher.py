from typing import Any, TypeVar

from ..utils.logging import get_logger

log = get_logger(__name__)

T = TypeVar("T", bound=dict[str, Any])


class DocPatch:
    KEY_MARKER_OVERLOAD_INDEX = "_PATCH_OVERLOAD_IDX"
    KEY_ACTION_REMOVE_NODE = "_PATCH_REMOVE_NODE"
    KEY_ACTION_REPLACE_NODE = "_PATCH_REPLACE_NODE"
    KEY_ACTION_REPLACE_FIELDS = "_PATCH_REPLACE_FIELDS"

    key_fields: dict[str, str]

    def __init__(self, key_fields):
        self.key_fields = key_fields

    def _decide_key_field(self, patch: T) -> str:
        for field in patch.keys():
            if field in self.key_fields.values():
                return field
        log.error(
            "failed to decide the key_field of patch\n"
            + f' > patch.keys: {",".join(patch.keys())}'
            + "   non is defined as key_fields for the patcher"
        )
        raise NotImplementedError()

    def patch(self, origin: T, patch: T):
        key_field = self._decide_key_field(patch)
        replace_fields = patch.pop(self.KEY_ACTION_REPLACE_FIELDS, None)
        for field, val in patch.items():
            if replace_fields is not None:
                if field in replace_fields:
                    log.debug(
                        "patching(REPLACE FIELDS) "
                        + f'{type(origin)}.{field} with value "{val}"'
                    )
                    origin[field] = val
            if field == key_field:
                # skip
                ...
            elif field in self.key_fields:
                if isinstance(val, dict):
                    self.patch(origin[field], val)
                elif isinstance(val, list):
                    self.patch_list(origin[field], val, self.key_fields[field])
                else:
                    raise NotImplementedError("unknown field:", field)
            else:
                log.debug(f'patching {type(origin)}.{field} with value "{val}"')
                origin[field] = val

    def patch_list(
        self,
        origin: list[T],
        patch: list[T],
        key_field: str,
        allow_append: bool = False,
    ):
        # FIXME: method overloads support
        item_map = {item[key_field]: item for item in origin}
        for item in patch:
            target = item[key_field]
            if target in item_map:
                if item.get(self.KEY_ACTION_REMOVE_NODE, False):
                    item.pop(self.KEY_ACTION_REMOVE_NODE)
                    log.debug(
                        "patching(REMOVE NODE) " + f'{type(origin)} with node "{item}"'
                    )
                    origin.remove(item_map.pop(target))
                elif item.get(self.KEY_ACTION_REPLACE_NODE, False):
                    item.pop(self.KEY_ACTION_REPLACE_NODE)
                    idx = origin.index(item_map[target])
                    log.debug(
                        "patching(REPLACE NODE) "
                        + f'{type(origin)}[{idx}] with node "{item}"'
                    )
                    origin[idx] = item
                    item_map[target] = item
                else:
                    self.patch(item_map[target], item)
            elif allow_append:
                log.debug(
                    "patching(APPEND NODE) " + f'{type(origin)} with node "{item}"'
                )
                origin.append(item)
            else:
                log.error(
                    "panic during patching!\n"
                    + f' > target "{target}" cannot be found with key field <{key_field}>'
                )
                raise NotImplementedError()
