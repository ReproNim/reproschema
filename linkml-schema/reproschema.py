from __future__ import annotations
from datetime import datetime, date
from decimal import Decimal
from enum import Enum

from typing import List, Dict, Optional, Any, Union
import pydantic as pyd
import re
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class ConfiguredBaseModel(pyd.BaseModel):
    model_config = pyd.ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra = 'forbid',
        arbitrary_types_allowed=True,
        use_enum_values = True)
    pass


class AdditionalNoteObj(ConfiguredBaseModel):
    """
    ['A set of objects to define notes in a field. For example, most Redcap and NDA data dictionaries have notes for each item which needs to be captured in reproschema']
    """
    column: Optional[List[str]] = pyd.Field(default_factory=list, title="column", description="""['An element to define the column name where the note was taken from.']""")
    source: Optional[List[str]] = pyd.Field(default_factory=list, title="source", description="""['An element to define the source (eg. RedCap, NDA) where the note was taken from.']""")
    value: Optional[List[Union[Decimal, LangString, StructuredValue, bool, str]]] = pyd.Field(default_factory=list, title="value", description="""['The value for each option in choices or in additionalNotesObj']""")
    
    

class AdditionalProperty(ConfiguredBaseModel):
    """
    ['An object to describe the various properties added to assessments and fields.']
    """
    allow: Optional[List[Thing]] = pyd.Field(default_factory=list, title="allow", description="""['An array of items indicating properties allowed on an activity or protocol ']""")
    isAbout: Optional[Union[Activity, Field]] = pyd.Field(None, title="isAbout", description="""['A pointer to the node describing the item.']""")
    isVis: Optional[Union[bool, str]] = pyd.Field(None, title="visibility", description="""['An element to describe (by boolean or conditional statement) visibility conditions of items in an assessment.']""")
    limit: Optional[LangString] = pyd.Field(None, title="limit", description="""['An element to limit the duration (uses ISO 8601) this activity is allowed to be completed by once activity is available.']""")
    maxRetakes: Optional[Decimal] = pyd.Field(None, title="maxRetakes", description="""['Defines number of times the item is allowed to be redone.']""")
    prefLabel: Optional[List[LangString]] = pyd.Field(default_factory=list, title="preferred label", description="""['The preferred label.']""")
    randomMaxDelay: Optional[LangString] = pyd.Field(None, title="randomMaxDelay", description="""['Present activity/item within some random offset of activity available time up to the maximum specified by this ISO 8601 duration']""")
    schedule: Optional[Union[Schedule, str]] = pyd.Field(None, title="Schedule", description="""['An element to set make activity available/repeat info using ISO 8601 repeating interval format.']""")
    valueRequired: Optional[bool] = pyd.Field(None)
    variableName: Optional[LangString] = pyd.Field(None, title="variableName", description="""['The name used to represent an item.']""")
    
    

class Agent(ConfiguredBaseModel):
    
    None
    
    

class AllowExport(ConfiguredBaseModel):
    """
    ['Indicates (by boolean) if data can be exported or not.']
    """
    None
    
    

class AllowReplay(ConfiguredBaseModel):
    """
    ['Indicates (by boolean) if items can be replayed or not.']
    """
    None
    
    

class AutoAdvance(ConfiguredBaseModel):
    """
    ['Indicates (by boolean) if assessments in a protocol can auto advance or not.']
    """
    None
    
    

class Choice(ConfiguredBaseModel):
    """
    ['An object to describe a response option.']
    """
    name: Optional[List[LangString]] = pyd.Field(default_factory=list)
    image: Optional[str] = pyd.Field(None, title="image", description="""['An image of the item. This can be a <a class=\"localLink\" href=\"http://schema.org/URL\">URL</a> or a fully described <a class=\"localLink\" href=\"http://schema.org/ImageObject\">ImageObject</a>.']""")
    value: Optional[List[Union[Decimal, LangString, StructuredValue, bool, str]]] = pyd.Field(default_factory=list, title="value", description="""['The value for each option in choices or in additionalNotesObj']""")
    
    

class ComputeSpecification(ConfiguredBaseModel):
    """
    ['An object to define computations in an activity or protocol.']
    """
    jsExpression: Optional[Union[LangString, bool]] = pyd.Field(None, title="JavaScript Expression", description="""['A JavaScript expression for computations.', 'A JavaScript expression to compute a score from other variables.']""")
    variableName: Optional[LangString] = pyd.Field(None, title="variableName", description="""['The name used to represent an item.']""")
    
    

class CreativeWork(ConfiguredBaseModel):
    
    None
    
    

class Activity(CreativeWork):
    """
    ['An assessment in a protocol.']
    """
    about: Optional[str] = pyd.Field(None, description="""['The subject matter of the Field.']""")
    altLabel: Optional[str] = pyd.Field(None, title="alternate label", description="""['The alternate label.']""")
    associatedMedia: Optional[str] = pyd.Field(None, title="associatedMedia", description="""['A media object that encodes this CreativeWork. This property is a synonym for encoding.']""")
    citation: Optional[LangString] = pyd.Field(None)
    compute: Optional[List[ComputeSpecification]] = pyd.Field(default_factory=list, title="computation", description="""['An array of objects indicating computations in an activity or protocol and maps it to the corresponding Field item. scoring logic is a subset of all computations that could be performed and not all computations will be scoring. For example, one may want to do conversion from one unit to another. ']""")
    cronTable: Optional[str] = pyd.Field(None, title="cronTable", description="""['TODO not described in reproschema']""")
    description: Optional[LangString] = pyd.Field(None)
    image: Optional[str] = pyd.Field(None, title="image", description="""['An image of the item. This can be a <a class=\"localLink\" href=\"http://schema.org/URL\">URL</a> or a fully described <a class=\"localLink\" href=\"http://schema.org/ImageObject\">ImageObject</a>.']""")
    messages: Optional[List[MessageSpecification]] = pyd.Field(default_factory=list, title="messages", description="""['An array of objects to define conditional messages in an activity or protocol.']""")
    preamble: Optional[List[LangString]] = pyd.Field(default_factory=list, title="Preamble", description="""['The preamble for an assessment']""")
    prefLabel: Optional[List[LangString]] = pyd.Field(default_factory=list, title="preferred label", description="""['The preferred label.']""")
    schemaVersion: Optional[LangString] = pyd.Field(None)
    ui: Optional[UiActivity] = pyd.Field(None, title="UI", description="""['it was originally @nest in jsonld, but decided for a new class for now']""")
    version: Optional[LangString] = pyd.Field(None)
    
    

class DisableBack(ConfiguredBaseModel):
    """
    ['Indicates (by boolean) if we can go back to a completed assessment in a protocol.']
    """
    None
    
    

class DontKnow(ConfiguredBaseModel):
    """
    ['An element to describe the choice when response is not known.']
    """
    None
    
    

class Field(CreativeWork):
    """
    ['An item in an assessment.']
    """
    about: Optional[str] = pyd.Field(None, description="""['The subject matter of the Field.']""")
    additionalNotesObj: Optional[List[AdditionalNoteObj]] = pyd.Field(default_factory=list, title="additional notes", description="""['A set of objects to define notes in a field. For example, most Redcap and NDA data dictionaries have notes for each item which needs to be captured in reproschema.']""")
    altLabel: Optional[str] = pyd.Field(None, title="alternate label", description="""['The alternate label.']""")
    associatedMedia: Optional[str] = pyd.Field(None, title="associatedMedia", description="""['A media object that encodes this CreativeWork. This property is a synonym for encoding.']""")
    audio: Optional[str] = pyd.Field(None, title="audio", description="""['TDOO']""")
    description: Optional[LangString] = pyd.Field(None)
    image: Optional[str] = pyd.Field(None, title="image", description="""['An image of the item. This can be a <a class=\"localLink\" href=\"http://schema.org/URL\">URL</a> or a fully described <a class=\"localLink\" href=\"http://schema.org/ImageObject\">ImageObject</a>.']""")
    imageUrl: Optional[str] = pyd.Field(None, title="imageUrl", description="""['An image url.']""")
    isPartOf: Optional[Activity] = pyd.Field(None)
    preamble: Optional[List[LangString]] = pyd.Field(default_factory=list, title="Preamble", description="""['The preamble for an assessment']""")
    prefLabel: Optional[List[LangString]] = pyd.Field(default_factory=list, title="preferred label", description="""['The preferred label.']""")
    question: Optional[List[LangString]] = pyd.Field(default_factory=list)
    responseOptions: Optional[Union[ResponseOption, str]] = pyd.Field(None, title="Response options", description="""['An element (object or by URL)to describe the properties of response of the Field item.']""")
    schemaVersion: Optional[LangString] = pyd.Field(None)
    ui: Optional[UiField] = pyd.Field(None, title="UI", description="""['it was originally @nest in jsonld, but decided for a new class for now']""")
    version: Optional[LangString] = pyd.Field(None)
    video: Optional[VideoObject] = pyd.Field(None)
    
    

class LandingPage(ConfiguredBaseModel):
    """
    ['An object to define the landing page of a protocol.']
    """
    inLanguage: Optional[List[LangString]] = pyd.Field(default_factory=list)
    
    

class LangString(ConfiguredBaseModel):
    
    None
    
    

class MediaObject(ConfiguredBaseModel):
    """
    ['TODO comments']
    """
    contentUrl: str = pyd.Field(...)
    inLanguage: Optional[List[LangString]] = pyd.Field(default_factory=list)
    
    

class MessageSpecification(ConfiguredBaseModel):
    """
    ['An object to define messages in an activity or protocol.']
    """
    jsExpression: Optional[Union[LangString, bool]] = pyd.Field(None, title="JavaScript Expression", description="""['A JavaScript expression for computations.', 'A JavaScript expression to compute a score from other variables.']""")
    message: Optional[List[LangString]] = pyd.Field(default_factory=list, title="Message", description="""['The message to be conditionally displayed for an item. ']""")
    
    

class OverrideProperty(ConfiguredBaseModel):
    """
    ['An object to override the various properties added to assessments and fields.']
    """
    isAbout: Optional[Union[Activity, Field]] = pyd.Field(None, title="isAbout", description="""['A pointer to the node describing the item.']""")
    isVis: Optional[Union[bool, str]] = pyd.Field(None, title="visibility", description="""['An element to describe (by boolean or conditional statement) visibility conditions of items in an assessment.']""")
    limit: Optional[LangString] = pyd.Field(None, title="limit", description="""['An element to limit the duration (uses ISO 8601) this activity is allowed to be completed by once activity is available.']""")
    maxRetakes: Optional[Decimal] = pyd.Field(None, title="maxRetakes", description="""['Defines number of times the item is allowed to be redone.']""")
    prefLabel: Optional[List[LangString]] = pyd.Field(default_factory=list, title="preferred label", description="""['The preferred label.']""")
    randomMaxDelay: Optional[LangString] = pyd.Field(None, title="randomMaxDelay", description="""['Present activity/item within some random offset of activity available time up to the maximum specified by this ISO 8601 duration']""")
    schedule: Optional[Union[Schedule, str]] = pyd.Field(None, title="Schedule", description="""['An element to set make activity available/repeat info using ISO 8601 repeating interval format.']""")
    valueRequired: Optional[bool] = pyd.Field(None)
    variableName: Optional[LangString] = pyd.Field(None, title="variableName", description="""['The name used to represent an item.']""")
    
    

class Participant(Agent):
    """
    ['An Agent describing characteristics associated with a participant.']
    """
    subject_id: Optional[LangString] = pyd.Field(None)
    
    

class Protocol(CreativeWork):
    """
    ['A representation of a study which comprises one or more assessments.']
    """
    about: Optional[str] = pyd.Field(None, description="""['The subject matter of the Field.']""")
    altLabel: Optional[str] = pyd.Field(None, title="alternate label", description="""['The alternate label.']""")
    associatedMedia: Optional[str] = pyd.Field(None, title="associatedMedia", description="""['A media object that encodes this CreativeWork. This property is a synonym for encoding.']""")
    compute: Optional[List[ComputeSpecification]] = pyd.Field(default_factory=list, title="computation", description="""['An array of objects indicating computations in an activity or protocol and maps it to the corresponding Field item. scoring logic is a subset of all computations that could be performed and not all computations will be scoring. For example, one may want to do conversion from one unit to another. ']""")
    cronTable: Optional[str] = pyd.Field(None, title="cronTable", description="""['TODO not described in reproschema']""")
    description: Optional[LangString] = pyd.Field(None)
    landingPage: Optional[Union[LandingPage, str]] = pyd.Field(None, title="Landing page content", description="""['An element (by URL) to point to the protocol readme or landing page.']""")
    messages: Optional[List[MessageSpecification]] = pyd.Field(default_factory=list, title="messages", description="""['An array of objects to define conditional messages in an activity or protocol.']""")
    prefLabel: Optional[List[LangString]] = pyd.Field(default_factory=list, title="preferred label", description="""['The preferred label.']""")
    schemaVersion: Optional[LangString] = pyd.Field(None)
    ui: Optional[UiProtocol] = pyd.Field(None, title="UI", description="""['it was originally @nest in jsonld, but decided for a new class for now']""")
    version: Optional[LangString] = pyd.Field(None)
    
    

class Response(CreativeWork):
    """
    ['Describes the response of an item.']
    """
    isAbout: Optional[Union[Activity, Field]] = pyd.Field(None, title="isAbout", description="""['A pointer to the node describing the item.']""")
    value: Optional[List[Union[Decimal, DontKnow, Skipped, StructuredValue, bool, str]]] = pyd.Field(default_factory=list, title="value", description="""['The value for each option in choices or in additionalNotesObj']""")
    wasAttributedTo: Optional[Participant] = pyd.Field(None)
    
    

class ResponseActivity(CreativeWork):
    """
    ['Captures information about some action that took place. It also links to information (entities) that were used during the activity']
    """
    endedAtTime: Optional[datetime ] = pyd.Field(None)
    generated: Optional[LangString] = pyd.Field(None)
    inLanguage: Optional[List[LangString]] = pyd.Field(default_factory=list)
    startedAtTime: Optional[datetime ] = pyd.Field(None)
    used: Optional[List[str]] = pyd.Field(default_factory=list)
    wasAssociatedWith: Optional[SoftwareAgent] = pyd.Field(None)
    
    

class ResponseOption(ConfiguredBaseModel):
    """
    ['An element (object or by URL)to describe the properties of response of the Field item.']
    """
    choices: Optional[List[Union[Choice, str]]] = pyd.Field(default_factory=list, title="choices", description="""['An array to list the available options for response of the Field item.']""")
    datumType: Optional[str] = pyd.Field(None, title="datumType", description="""['Indicates what type of datum the response is (e.g. range,count,scalar etc.) for the Field item.']""")
    maxValue: Optional[Union[float, int]] = pyd.Field(None)
    minValue: Optional[Union[float, int]] = pyd.Field(None)
    multipleChoice: Optional[bool] = pyd.Field(None, title="Multiple choice response expectation", description="""['Indicates (by bool) if response for the Field item has one or more answer.']""")
    unitOptions: Optional[List[UnitOption]] = pyd.Field(default_factory=list, title="unitOptions", description="""['A list of objects to represent a human displayable name alongside the more formal value for units.']""")
    valueType: Optional[List[str]] = pyd.Field(default_factory=list, title="The type of the response", description="""['The type of the response of an item. For example, string, integer, etc.']""")
    
    

class Schedule(ConfiguredBaseModel):
    """
    ['An object to define the schedule of an activity or protocol.']
    """
    None
    
    

class Skipped(ConfiguredBaseModel):
    """
    ['An element to describe the choice when the item is skipped.']
    """
    None
    
    

class SoftwareAgent(ConfiguredBaseModel):
    """
    ['Captures information about some action that took place. It also links to information (entities) that were used during the activity']
    """
    version: Optional[LangString] = pyd.Field(None)
    url: Optional[str] = pyd.Field(None)
    
    

class StructuredValue(ConfiguredBaseModel):
    
    None
    
    

class Thing(ConfiguredBaseModel):
    
    None
    
    

class TimedOut(ConfiguredBaseModel):
    """
    ['A boolean element to describe if the response did not occur within the prescribed time.']
    """
    None
    
    

class UiActivity(ConfiguredBaseModel):
    """
    ['todo']
    """
    order: Optional[List[Union[Activity, Field, str]]] = pyd.Field(default_factory=list, title="Order", description="""['An ordered list to describe the order in which the items of an assessment or protocol appear in the user interface.']""")
    addProperties: Optional[List[AdditionalProperty]] = pyd.Field(default_factory=list, title="addProperties", description="""['An array of objects to describe the various properties added to assessments and fields.']""")
    overrideProperties: Optional[List[OverrideProperty]] = pyd.Field(default_factory=list, title="overrideProperties", description="""['An array of objects to override the various properties added to assessments and fields.']""")
    shuffle: Optional[bool] = pyd.Field(None, title="Shuffle", description="""['An element (bool) to determine if the list of items is shuffled or in order.']""")
    allow: Optional[List[Thing]] = pyd.Field(default_factory=list, title="allow", description="""['An array of items indicating properties allowed on an activity or protocol ']""")
    
    

class UiField(ConfiguredBaseModel):
    """
    ['todo']
    """
    inputType: Optional[str] = pyd.Field(None, title="inputType", description="""['An element to describe the input type of a Field item.']""")
    readonlyValue: Optional[bool] = pyd.Field(None)
    
    

class UiProtocol(ConfiguredBaseModel):
    """
    ['todo']
    """
    order: Optional[List[Union[Activity, Field, str]]] = pyd.Field(default_factory=list, title="Order", description="""['An ordered list to describe the order in which the items of an assessment or protocol appear in the user interface.']""")
    addProperties: Optional[List[AdditionalProperty]] = pyd.Field(default_factory=list, title="addProperties", description="""['An array of objects to describe the various properties added to assessments and fields.']""")
    overrideProperties: Optional[List[OverrideProperty]] = pyd.Field(default_factory=list, title="overrideProperties", description="""['An array of objects to override the various properties added to assessments and fields.']""")
    shuffle: Optional[bool] = pyd.Field(None, title="Shuffle", description="""['An element (bool) to determine if the list of items is shuffled or in order.']""")
    allow: Optional[List[Thing]] = pyd.Field(default_factory=list, title="allow", description="""['An array of items indicating properties allowed on an activity or protocol ']""")
    
    

class UnitOption(ConfiguredBaseModel):
    """
    ['An object to represent a human displayable name alongside the more formal value for units.']
    """
    prefLabel: Optional[List[LangString]] = pyd.Field(default_factory=list, title="preferred label", description="""['The preferred label.']""")
    value: Optional[List[Union[LangString, str]]] = pyd.Field(default_factory=list, title="value", description="""['The value for each option in choices or in additionalNotesObj']""")
    
    

class VideoObject(ConfiguredBaseModel):
    
    contentUrl: str = pyd.Field(...)
    inLanguage: Optional[List[LangString]] = pyd.Field(default_factory=list)
    
    


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AdditionalNoteObj.model_rebuild()
AdditionalProperty.model_rebuild()
Agent.model_rebuild()
AllowExport.model_rebuild()
AllowReplay.model_rebuild()
AutoAdvance.model_rebuild()
Choice.model_rebuild()
ComputeSpecification.model_rebuild()
CreativeWork.model_rebuild()
Activity.model_rebuild()
DisableBack.model_rebuild()
DontKnow.model_rebuild()
Field.model_rebuild()
LandingPage.model_rebuild()
LangString.model_rebuild()
MediaObject.model_rebuild()
MessageSpecification.model_rebuild()
OverrideProperty.model_rebuild()
Participant.model_rebuild()
Protocol.model_rebuild()
Response.model_rebuild()
ResponseActivity.model_rebuild()
ResponseOption.model_rebuild()
Schedule.model_rebuild()
Skipped.model_rebuild()
SoftwareAgent.model_rebuild()
StructuredValue.model_rebuild()
Thing.model_rebuild()
TimedOut.model_rebuild()
UiActivity.model_rebuild()
UiField.model_rebuild()
UiProtocol.model_rebuild()
UnitOption.model_rebuild()
VideoObject.model_rebuild()

