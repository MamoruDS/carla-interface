from typing import Any, TypeVar

T = TypeVar("T", bound=dict[str, Any])


class DocPatch:
    KEY_MARKER_OVERLOAD_INDEX = "_PATCH_OVERLOAD_IDX"
    KEY_ACTION_REMOVE_NODE = "_PATCH_REMOVE_NODE"
    KEY_ACTION_REPLACE_NODE = "_PATCH_REPLACE_NODE"
    KEY_ACTION_REPLACE_FIELDS = "_PATCH_REPLACE_FIELDS"

    key_fields: dict[str, str]

    def __init__(self, key_fields):
        self.key_fields = key_fields

    def patch(self, origin: T, patch: T):
        replace_fields = patch.pop(self.KEY_ACTION_REPLACE_FIELDS, None)
        for field, val in patch.items():
            if replace_fields is not None:
                if field in replace_fields:
                    origin[field] = val
            if field in self.key_fields:
                if isinstance(val, dict):
                    self.patch(origin[field], val)
                elif isinstance(val, list):
                    self.patch_list(origin[field], val, self.key_fields[field])
                else:
                    raise NotImplementedError("unknown field:", field)
            elif field in self.key_fields.values():
                ...
            else:
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
                    origin.remove(item_map.pop(target))
                elif item.get(self.KEY_ACTION_REPLACE_NODE, False):
                    item.pop(self.KEY_ACTION_REPLACE_NODE)
                    idx = origin.index(item_map[target])
                    origin[idx] = item
                    item_map[target] = item
                else:
                    self.patch(item_map[target], item)
            elif allow_append:
                origin.append(item)
