from typing import Any, TypeVar

T = TypeVar("T", bound=dict[str, Any])


class DocPatch:
    key_fields: dict[str, str]

    def __init__(self, key_fields):
        self.key_fields = key_fields

    def patch(self, origin: T, patch: T):
        for field, val in patch.items():
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
        item_map = {item[key_field]: item for item in origin}
        for item in patch:
            if item[key_field] in item_map:
                self.patch(item_map[item[key_field]], item)
            elif allow_append:
                origin.append(item)
