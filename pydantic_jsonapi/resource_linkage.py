from typing import Optional, Union, List

from pydantic import BaseModel

from pydantic_jsonapi.resource_identifier import ResourceIdentifier

ResourceLinkage = Optional[Union[ResourceIdentifier, List[ResourceIdentifier]]]
