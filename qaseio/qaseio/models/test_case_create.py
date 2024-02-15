# coding: utf-8

"""
    Qase.io TestOps API

    Qase TestOps API Specification.

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from qaseio.models.test_step_create import TestStepCreate
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TestCaseCreate(BaseModel):
    """
    TestCaseCreate
    """ # noqa: E501
    description: Optional[StrictStr] = None
    preconditions: Optional[StrictStr] = None
    postconditions: Optional[StrictStr] = None
    title: Annotated[str, Field(strict=True, max_length=255)]
    severity: Optional[StrictInt] = None
    priority: Optional[StrictInt] = None
    behavior: Optional[StrictInt] = None
    type: Optional[StrictInt] = None
    layer: Optional[StrictInt] = None
    is_flaky: Optional[StrictInt] = None
    author_id: Optional[StrictInt] = None
    suite_id: Optional[StrictInt] = None
    milestone_id: Optional[StrictInt] = None
    automation: Optional[StrictInt] = None
    status: Optional[StrictInt] = None
    attachments: Optional[List[StrictStr]] = Field(default=None, description="A list of Attachment hashes.")
    steps: Optional[List[TestStepCreate]] = None
    tags: Optional[List[StrictStr]] = None
    params: Optional[Dict[str, List[StrictStr]]] = None
    custom_field: Optional[Dict[str, StrictStr]] = Field(default=None, description="A map of custom fields values (id => value)")
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["description", "preconditions", "postconditions", "title", "severity", "priority", "behavior", "type", "layer", "is_flaky", "author_id", "suite_id", "milestone_id", "automation", "status", "attachments", "steps", "tags", "params", "custom_field", "created_at", "updated_at"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestCaseCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item in self.steps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['steps'] = _items
        # set to None if params (nullable) is None
        # and model_fields_set contains the field
        if self.params is None and "params" in self.model_fields_set:
            _dict['params'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TestCaseCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "preconditions": obj.get("preconditions"),
            "postconditions": obj.get("postconditions"),
            "title": obj.get("title"),
            "severity": obj.get("severity"),
            "priority": obj.get("priority"),
            "behavior": obj.get("behavior"),
            "type": obj.get("type"),
            "layer": obj.get("layer"),
            "is_flaky": obj.get("is_flaky"),
            "author_id": obj.get("author_id"),
            "suite_id": obj.get("suite_id"),
            "milestone_id": obj.get("milestone_id"),
            "automation": obj.get("automation"),
            "status": obj.get("status"),
            "attachments": obj.get("attachments"),
            "steps": [TestStepCreate.from_dict(_item) for _item in obj.get("steps")] if obj.get("steps") is not None else None,
            "tags": obj.get("tags"),
            "params": obj.get("params"),
            "custom_field": obj.get("custom_field"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


