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

    def _decide_key_field(self, patch: dict[str, Any]) -> str:
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
                if field not in origin:
                    log.error(
                        'failed to patch origin("{}") without key_field "{}"'.format(
                            key_field, field
                        )
                    )
                    origin[field]  # never
                if isinstance(val, dict):
                    self.patch(origin[field], val)
                elif isinstance(val, list):
                    self.patch_list(origin[field], val, self.key_fields[field])
                else:
                    # TODO:
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
        item_map: dict[str, list[T]] = {}
        for item in origin:
            item_map.setdefault(item[key_field], []).append(item)
        for item in patch:
            target: str = item[key_field]
            overload_idx: int | None = item.pop(self.KEY_MARKER_OVERLOAD_INDEX, None)
            if target in item_map:
                if item.get(self.KEY_ACTION_REMOVE_NODE, False):
                    item.pop(self.KEY_ACTION_REMOVE_NODE)
                    log.debug(
                        "patching(REMOVE NODE) " + f'{type(origin)} with node "{item}"'
                    )

                    for oi, overload in enumerate(item_map[target]):
                        if overload_idx is None or oi == overload_idx:
                            origin.remove(overload)
                            item_map[target].remove(overload)
                elif item.get(self.KEY_ACTION_REPLACE_NODE, False):
                    item.pop(self.KEY_ACTION_REPLACE_NODE)
                    for oi, overload in enumerate(item_map[target]):
                        if overload_idx is None or oi == overload_idx:
                            idx = origin.index(overload)
                            log.debug(
                                "patching(REPLACE NODE) "
                                + f'{type(origin)}[{idx}] with node "{item}"'
                            )
                            origin[idx] = item
                            item_map[target][oi] = item
                else:
                    for oi, overload in enumerate(item_map[target]):
                        if overload_idx is None or oi == overload_idx:
                            try:
                                self.patch(overload, item)
                            except Exception as err:
                                log.error(
                                    f'failed to patch overload[{oi}] ("{key_field}")\n'
                                    + f" > overload_idx : {overload_idx}\n"
                                    + f' > overload.keys: {", ".join(overload)}\n'
                                    + f' > item.keys    : {", ".join(item)}'
                                )
                                raise err
            elif allow_append:
                log.debug(
                    "patching(APPEND NODE) " + f'{type(origin)} with node "{item}"'
                )
                origin.append(item)
                item_map.setdefault(target, []).append(item)
            else:
                log.error(
                    "panic during patching!\n"
                    + f' > target "{target}" cannot be found with key field <{key_field}>'
                )
                raise NotImplementedError()
