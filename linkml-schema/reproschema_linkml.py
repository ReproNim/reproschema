from __future__ import annotations
from datetime import datetime, date
from enum import Enum

from decimal import Decimal
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, ConfigDict,  Field, field_validator
import re
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra = 'forbid',
        arbitrary_types_allowed=True,
        use_enum_values = True)

    pass



class AllowedType(str, Enum):

    # Indicates (by boolean) if alternate responses are allowed or not.
    AllowAltResponse = "reproschema:AllowAltResponse"
    # Indicates (by boolean) if data can be exported or not.
    AllowExport = "reproschema:AllowExport"
    # Indicates (by boolean) if items can be replayed or not.
    AllowReplay = "reproschema:AllowReplay"
    # Indicates (by boolean) if items can be skipped or not.
    AllowSkip = "reproschema:AllowSkip"
    # Indicates (by boolean) if assessments in a protocol can auto advance or not.
    AutoAdvance = "reproschema:AutoAdvance"
    # Indicates (by boolean) if we can go back to a completed assessment in a protocol.
    DisableBack = "reproschema:DisableBack"


class MissingType(str, Enum):
    # An element to describe the choice when the item is skipped.
    Skipped = "reproschema:Skipped"
    # An element to describe the choice when response is not known.
    DontKnow = "reproschema:DontKnow"
    # An element to describe the choice when the reason for missing response is unknown.
    Unknown = "reproschema:Unknown"
    # A boolean element to describe if the response did not occur within the prescribed time.
    TimedOut = "reproschema:TimedOut"



class AdditionalNoteObj(ConfiguredBaseModel):
    """
    A set of objects to define notes in a Item. For example, most Redcap and NDA data dictionaries have notes for each item which needs to be captured in reproschema
    """
    column: Optional[str] = Field(None, title="column", description="""An element to define the column name where the note was taken from.""")
    source: Optional[str] = Field(None, title="source", description="""An element to define the source (eg. RedCap, NDA) where the note was taken from.""")
    value: Optional[Union[Decimal, Dict[str, str], MissingType, StructuredValue, bool, str]] = Field(None, title="value", description="""The value for each option in choices or in additionalNotesObj""")
    
    

class AdditionalProperty(ConfiguredBaseModel):
    """
    An object to describe the various properties added to assessments and Items.
    """
    allow: Optional[List[AllowedType]] = Field(default_factory=list, title="allow", description="""An array of items indicating properties allowed on an activity or protocol.""")
    isAbout: Optional[Union[Activity, Item, str]] = Field(None, title="isAbout", description="""A pointer to the node describing the item.""")
    isVis: Optional[Union[bool, str]] = Field(None, title="visibility", description="""An element to describe (by boolean or conditional statement) visibility conditions of items in an assessment.""")
    limit: Optional[str] = Field(None, title="limit", description="""An element to limit the duration (uses ISO 8601) this activity is allowed to be completed by once activity is available.""")
    maxRetakes: Optional[Decimal] = Field(None, title="maxRetakes", description="""Defines number of times the item is allowed to be redone.""")
    prefLabel: Optional[Dict[str, str]] = Field(default_factory=dict, title="preferred label", description="""The preferred label.""")
    randomMaxDelay: Optional[str] = Field(None, title="randomMaxDelay", description="""Present activity/item within some random offset of activity available time up to the maximum specified by this ISO 8601 duration""")
    schedule: Optional[str] = Field(None, title="Schedule", description="""An element to set make activity available/repeat info using ISO 8601 repeating interval format.""")
    valueRequired: Optional[bool] = Field(None)
    variableName: Optional[str] = Field(None, title="variableName", description="""The name used to represent an item.""")
    ui: Optional[UI] = Field(None, title="UI", description="""An element to control UI specifications. Originally @nest in jsonld, but using a class in the model.""")
    
    

class Agent(ConfiguredBaseModel):
    
    None
    
    

class Choice(ConfiguredBaseModel):
    """
    An object to describe a response option.
    """
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    image: Optional[Union[ImageObject, str]] = Field(None, title="image", description="""An image of the item. This can be a <a class=\"localLink\" href=\"http://schema.org/URL\">URL</a> or a fully described <a class=\"localLink\" href=\"http://schema.org/ImageObject\">ImageObject</a>.""")
    value: Optional[Union[Decimal, Dict[str, str], MissingType, StructuredValue, bool, str]] = Field(None, title="value", description="""The value for each option in choices or in additionalNotesObj""")
    
    

class ComputeSpecification(ConfiguredBaseModel):
    """
    An object to define computations in an activity or protocol.
    """
    jsExpression: Optional[str] = Field(None, title="JavaScript Expression", description="""A JavaScript expression for computations. A JavaScript expression to compute a score from other variables.""")
    variableName: Optional[str] = Field(None, title="variableName", description="""The name used to represent an item.""")
    
    

class CreativeWork(ConfiguredBaseModel):
    
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class Activity(CreativeWork):
    """
    An assessment in a protocol.
    """
    about: Optional[str] = Field(None, description="""The subject matter of the Field.""")
    altLabel: Optional[Dict[str, str]] = Field(default_factory=dict, title="alternate label", description="""The alternate label.""")
    associatedMedia: Optional[str] = Field(None, title="associatedMedia", description="""A media object that encodes this CreativeWork. This property is a synonym for encoding.""")
    citation: Optional[Dict[str, str]] = Field(default_factory=dict)
    compute: Optional[List[ComputeSpecification]] = Field(default_factory=list, title="computation", description="""An array of objects indicating computations in an activity or protocol and maps it to the corresponding Item. scoring logic is a subset of all computations that could be performed and not all computations will be scoring. For example, one may want to do conversion from one unit to another.""")
    cronTable: Optional[str] = Field(None, title="cronTable", description="""TODO not described in reproschema""")
    description: Optional[Dict[str, str]] = Field(default_factory=dict)
    image: Optional[Union[ImageObject, str]] = Field(None, title="image", description="""An image of the item. This can be a <a class=\"localLink\" href=\"http://schema.org/URL\">URL</a> or a fully described <a class=\"localLink\" href=\"http://schema.org/ImageObject\">ImageObject</a>.""")
    messages: Optional[List[MessageSpecification]] = Field(default_factory=list, title="messages", description="""An array of objects to define conditional messages in an activity or protocol.""")
    preamble: Optional[Dict[str, str]] = Field(default_factory=dict, title="Preamble", description="""The preamble for an assessment""")
    prefLabel: Optional[Dict[str, str]] = Field(default_factory=dict, title="preferred label", description="""The preferred label.""")
    schemaVersion: Optional[str] = Field(None)
    ui: Optional[UI] = Field(None, title="UI", description="""An element to control UI specifications. Originally @nest in jsonld, but using a class in the model.""")
    version: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class Item(CreativeWork):
    """
    An item in an assessment.
    """
    about: Optional[str] = Field(None, description="""The subject matter of the Field.""")
    additionalNotesObj: Optional[List[AdditionalNoteObj]] = Field(default_factory=list, title="additional notes", description="""A set of objects to define notes in a field. For example, most Redcap and NDA data dictionaries have notes for each item which needs to be captured in reproschema.""")
    altLabel: Optional[Dict[str, str]] = Field(default_factory=dict, title="alternate label", description="""The alternate label.""")
    associatedMedia: Optional[str] = Field(None, title="associatedMedia", description="""A media object that encodes this CreativeWork. This property is a synonym for encoding.""")
    audio: Optional[Union[AudioObject, str]] = Field(None, title="audio", description="""TODO""")
    description: Optional[Dict[str, str]] = Field(default_factory=dict)
    image: Optional[Union[ImageObject, str]] = Field(None, title="image", description="""An image of the item. This can be a <a class=\"localLink\" href=\"http://schema.org/URL\">URL</a> or a fully described <a class=\"localLink\" href=\"http://schema.org/ImageObject\">ImageObject</a>.""")
    imageUrl: Optional[str] = Field(None, title="imageUrl", description="""An image url.""")
    isPartOf: Optional[Activity] = Field(None)
    preamble: Optional[Dict[str, str]] = Field(default_factory=dict, title="Preamble", description="""The preamble for an assessment""")
    prefLabel: Optional[Dict[str, str]] = Field(default_factory=dict, title="preferred label", description="""The preferred label.""")
    question: Optional[Dict[str, str]] = Field(default_factory=dict)
    responseOptions: Optional[Union[ResponseOption, str]] = Field(None, title="Response options", description="""An element (object or by URL)to describe the properties of response of the Item.""")
    schemaVersion: Optional[str] = Field(None)
    ui: Optional[UI] = Field(None, title="UI", description="""An element to control UI specifications. Originally @nest in jsonld, but using a class in the model.""")
    version: Optional[str] = Field(None)
    video: Optional[VideoObject] = Field(None)
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class LandingPage(ConfiguredBaseModel):
    """
    An object to define the landing page of a protocol.
    """
    inLanguage: Optional[str] = Field(None)
    id: Optional[str] = Field(None)

    

class MediaObject(CreativeWork):
    """
    Add description
    """
    contentUrl: str = Field(...)
    inLanguage: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class AudioObject(MediaObject):
    
    contentUrl: str = Field(...)
    inLanguage: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class ImageObject(MediaObject):
    
    contentUrl: str = Field(...)
    inLanguage: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class MessageSpecification(ConfiguredBaseModel):
    """
    An object to define messages in an activity or protocol.
    """
    jsExpression: Optional[str] = Field(None, title="JavaScript Expression", description="""A JavaScript expression for computations. A JavaScript expression to compute a score from other variables.""")
    message: Optional[Dict[str, str]] = Field(default_factory=dict, title="Message", description="""The message to be conditionally displayed for an item.""")
    
    

class OverrideProperty(ConfiguredBaseModel):
    """
    An object to override the various properties added to assessments and Items.
    """
    isAbout: Optional[Union[Activity, Item, str]] = Field(None, title="isAbout", description="""A pointer to the node describing the item.""")
    isVis: Optional[Union[bool, str]] = Field(None, title="visibility", description="""An element to describe (by boolean or conditional statement) visibility conditions of items in an assessment.""")
    limit: Optional[str] = Field(None, title="limit", description="""An element to limit the duration (uses ISO 8601) this activity is allowed to be completed by once activity is available.""")
    maxRetakes: Optional[Decimal] = Field(None, title="maxRetakes", description="""Defines number of times the item is allowed to be redone.""")
    prefLabel: Optional[Dict[str, str]] = Field(default_factory=dict, title="preferred label", description="""The preferred label.""")
    randomMaxDelay: Optional[str] = Field(None, title="randomMaxDelay", description="""Present activity/item within some random offset of activity available time up to the maximum specified by this ISO 8601 duration""")
    schedule: Optional[str] = Field(None, title="Schedule", description="""An element to set make activity available/repeat info using ISO 8601 repeating interval format.""")
    valueRequired: Optional[bool] = Field(None)
    variableName: Optional[str] = Field(None, title="variableName", description="""The name used to represent an item.""")
    
    

class Participant(Agent):
    """
    An Agent describing characteristics associated with a participant.
    """
    subject_id: Optional[str] = Field(None)
    
    

class Protocol(CreativeWork):
    """
    A representation of a study which comprises one or more assessments.
    """
    about: Optional[str] = Field(None, description="""The subject matter of the Field.""")
    altLabel: Optional[Dict[str, str]] = Field(default_factory=dict, title="alternate label", description="""The alternate label.""")
    associatedMedia: Optional[str] = Field(None, title="associatedMedia", description="""A media object that encodes this CreativeWork. This property is a synonym for encoding.""")
    compute: Optional[List[ComputeSpecification]] = Field(default_factory=list, title="computation", description="""An array of objects indicating computations in an activity or protocol and maps it to the corresponding Item. scoring logic is a subset of all computations that could be performed and not all computations will be scoring. For example, one may want to do conversion from one unit to another.""")
    cronTable: Optional[str] = Field(None, title="cronTable", description="""TODO not described in reproschema""")
    description: Optional[Dict[str, str]] = Field(default_factory=dict)
    landingPage: Optional[List[Union[LandingPage, str]]] = Field(default_factory=list, title="Landing page content", description="""An element (by URL) to point to the protocol readme or landing page.""")
    messages: Optional[List[MessageSpecification]] = Field(default_factory=list, title="messages", description="""An array of objects to define conditional messages in an activity or protocol.""")
    prefLabel: Optional[Dict[str, str]] = Field(default_factory=dict, title="preferred label", description="""The preferred label.""")
    schemaVersion: Optional[str] = Field(None)
    ui: Optional[UI] = Field(None, title="UI", description="""An element to control UI specifications. Originally @nest in jsonld, but using a class in the model.""")
    version: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class Response(CreativeWork):
    """
    Describes the response of an item.
    """
    isAbout: Optional[Union[Activity, Item, str]] = Field(None, title="isAbout", description="""A pointer to the node describing the item.""")
    value: Optional[Union[Decimal, Dict[str, str], MissingType, StructuredValue, bool, str]] = Field(None, title="value", description="""The value for each option in choices or in additionalNotesObj""")
    wasAttributedTo: Optional[Participant] = Field(None)
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class ResponseActivity(CreativeWork):
    """
    Captures information about some action that took place. It also links to information (entities) that were used during the activity
    """
    endedAtTime: Optional[datetime ] = Field(None)
    generated: Optional[str] = Field(None)
    inLanguage: Optional[str] = Field(None)
    startedAtTime: Optional[datetime ] = Field(None)
    used: Optional[List[str]] = Field(default_factory=list)
    wasAssociatedWith: Optional[SoftwareAgent] = Field(None)
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class ResponseOption(CreativeWork):
    """
    An element (object or by URL)to describe the properties of response of the Item.
    """
    choices: Optional[List[Union[Choice, str]]] = Field(default_factory=list, title="choices", description="""An array to list the available options for response of the Item.""")
    datumType: Optional[str] = Field(None, title="datumType", description="""Indicates what type of datum the response is (e.g. range,count,scalar etc.) for the Item.""")
    maxValue: Optional[Union[float, int]] = Field(None)
    minValue: Optional[Union[float, int]] = Field(None)
    multipleChoice: Optional[bool] = Field(None, title="Multiple choice response expectation", description="""Indicates (by bool) if response for the Item has one or more answer.""")
    unitOptions: Optional[List[UnitOption]] = Field(default_factory=list, title="unitOptions", description="""A list of objects to represent a human displayable name alongside the more formal value for units.""")
    valueType: Optional[List[str]] = Field(default_factory=list, title="The type of the response", description="""The type of the response of an item. For example, string, integer, etc.""")
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class SoftwareAgent(ConfiguredBaseModel):
    """
    Captures information about some action that took place. It also links to information (entities) that were used during the activity
    """
    version: Optional[str] = Field(None)
    url: Optional[str] = Field(None)
    
    

class StructuredValue(CreativeWork):
    
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    

class Thing(ConfiguredBaseModel):
    
    None
    
    

class UI(ConfiguredBaseModel):
    """
    ['todo']
    """
    order: Optional[List[Union[Activity, Item, str]]] = Field(default_factory=list, title="Order", description="""An ordered list to describe the order in which the items of an assessment or protocol appear in the user interface.""")
    addProperties: Optional[List[AdditionalProperty]] = Field(default_factory=list, title="addProperties", description="""An array of objects to describe the various properties added to assessments and Items.""")
    overrideProperties: Optional[List[OverrideProperty]] = Field(default_factory=list, title="overrideProperties", description="""An array of objects to override the various properties added to assessments and fields.""")
    shuffle: Optional[bool] = Field(None, title="Shuffle", description="""An element (bool) to determine if the list of items is shuffled or in order.""")
    allow: Optional[List[AllowedType]] = Field(default_factory=list, title="allow", description="""An array of items indicating properties allowed on an activity or protocol.""")
    inputType: Optional[str] = Field(None, title="inputType", description="""An element to describe the input type of a Item.""")
    readonlyValue: Optional[bool] = Field(None)
    
    

class UnitOption(ConfiguredBaseModel):
    """
    An object to represent a human displayable name alongside the more formal value for units.
    """
    prefLabel: Optional[Dict[str, str]] = Field(default_factory=dict, title="preferred label", description="""The preferred label.""")
    value: Optional[Union[Dict[str, str], str]] = Field(None, title="value", description="""The value for each option in choices or in additionalNotesObj""")
    
    

class VideoObject(MediaObject):
    
    contentUrl: str = Field(...)
    inLanguage: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    
    


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AdditionalNoteObj.model_rebuild()
AdditionalProperty.model_rebuild()
Agent.model_rebuild()
Choice.model_rebuild()
ComputeSpecification.model_rebuild()
CreativeWork.model_rebuild()
Activity.model_rebuild()
Item.model_rebuild()
LandingPage.model_rebuild()
MediaObject.model_rebuild()
AudioObject.model_rebuild()
ImageObject.model_rebuild()
MessageSpecification.model_rebuild()
OverrideProperty.model_rebuild()
Participant.model_rebuild()
Protocol.model_rebuild()
Response.model_rebuild()
ResponseActivity.model_rebuild()
ResponseOption.model_rebuild()
SoftwareAgent.model_rebuild()
StructuredValue.model_rebuild()
Thing.model_rebuild()
UI.model_rebuild()
UnitOption.model_rebuild()
VideoObject.model_rebuild()

