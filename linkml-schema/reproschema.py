from __future__ import annotations
from datetime import datetime, date
from enum import Enum

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


class AdditionalNoteObj(ConfiguredBaseModel):
    
    column: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="column")
    source: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="source")
    value: Optional[List[Union[Decimal, LangString, StructuredValue, bool, str]]] = Field(default_factory=list, title="value")
    
    

class AdditionalProperty(ConfiguredBaseModel):
    
    allow: Optional[List[Thing]] = Field(default_factory=list, title="allow")
    isAbout: Optional[Union[Activity, Field]] = Field(None, title="isAbout")
    isVis: Optional[Union[bool, str]] = Field(None, title="visibility")
    limit: Optional[str] = Field(None, title="limit")
    maxRetakes: Optional[Decimal] = Field(None, title="maxRetakes")
    prefLabel: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="preferred label")
    randomMaxDelay: Optional[str] = Field(None, title="randomMaxDelay")
    schedule: Optional[Union[Schedule, str]] = Field(None, title="Schedule")
    valueRequired: Optional[bool] = Field(None)
    variableName: Optional[str] = Field(None, title="variableName")
    
    

class Agent(ConfiguredBaseModel):
    
    None
    
    

class AllowExport(ConfiguredBaseModel):
    
    None
    
    

class AllowReplay(ConfiguredBaseModel):
    
    None
    
    

class AutoAdvance(ConfiguredBaseModel):
    
    None
    
    

class Choice(ConfiguredBaseModel):
    
    name: Optional[List[Union[LangString, str]]] = Field(default_factory=list)
    image: Optional[str] = Field(None, title="image")
    value: Optional[List[Union[Decimal, LangString, StructuredValue, bool, str]]] = Field(default_factory=list, title="value")
    
    

class ComputeSpecification(ConfiguredBaseModel):
    
    jsExpression: Optional[Union[bool, str]] = Field(None, title="JavaScript Expression")
    variableName: Optional[str] = Field(None, title="variableName")
    
    

class CreativeWork(ConfiguredBaseModel):
    
    None
    
    

class Activity(CreativeWork):
    
    about: Optional[str] = Field(None)
    addProperties: Optional[List[AdditionalProperty]] = Field(default_factory=list, title="addProperties")
    allow: Optional[List[Thing]] = Field(default_factory=list, title="allow")
    altLabel: Optional[str] = Field(None, title="alternate label")
    associatedMedia: Optional[str] = Field(None, title="associatedMedia")
    citation: Optional[str] = Field(None)
    compute: Optional[List[ComputeSpecification]] = Field(default_factory=list, title="computation")
    cronTable: Optional[str] = Field(None, title="cronTable")
    description: Optional[str] = Field(None)
    image: Optional[str] = Field(None, title="image")
    messages: Optional[List[MessageSpecification]] = Field(default_factory=list, title="messages")
    order: Optional[List[Union[Activity, Field, str]]] = Field(default_factory=list, title="Order")
    overrideProperties: Optional[List[OverrideProperty]] = Field(default_factory=list, title="overrideProperties")
    preamble: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="Preamble")
    prefLabel: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="preferred label")
    schemaVersion: Optional[str] = Field(None)
    shuffle: Optional[bool] = Field(None, title="Shuffle")
    ui: Optional[UI] = Field(None, title="UI")
    version: Optional[str] = Field(None)
    
    

class DisableBack(ConfiguredBaseModel):
    
    None
    
    

class DontKnow(ConfiguredBaseModel):
    
    None
    
    

class Field(CreativeWork):
    
    about: Optional[str] = Field(None)
    additionalNotesObj: Optional[List[AdditionalNoteObj]] = Field(default_factory=list, title="additional notes")
    altLabel: Optional[str] = Field(None, title="alternate label")
    associatedMedia: Optional[str] = Field(None, title="associatedMedia")
    audio: Optional[str] = Field(None, title="audio")
    description: Optional[str] = Field(None)
    image: Optional[str] = Field(None, title="image")
    inputType: Optional[str] = Field(None, title="inputType")
    isPartOf: Optional[Activity] = Field(None)
    preamble: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="Preamble")
    prefLabel: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="preferred label")
    question: Optional[List[Union[LangString, str]]] = Field(default_factory=list)
    readonlyValue: Optional[str] = Field(None)
    responseOptions: Optional[Union[ResponseOption, str]] = Field(None, title="Response options")
    schemaVersion: Optional[str] = Field(None)
    ui: Optional[UI] = Field(None, title="UI")
    version: Optional[str] = Field(None)
    video: Optional[VideoObject] = Field(None)
    
    

class LandingPage(ConfiguredBaseModel):
    
    inLanguage: Optional[List[Union[LangString, str]]] = Field(default_factory=list)
    
    

class LangString(ConfiguredBaseModel):
    
    None
    
    

class MediaObject(ConfiguredBaseModel):
    
    contentUrl: str = Field(...)
    inLanguage: Optional[List[Union[LangString, str]]] = Field(default_factory=list)
    
    

class MessageSpecification(ConfiguredBaseModel):
    
    jsExpression: Optional[Union[bool, str]] = Field(None, title="JavaScript Expression")
    message: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="Message")
    
    

class OverrideProperty(ConfiguredBaseModel):
    
    isAbout: Optional[Union[Activity, Field]] = Field(None, title="isAbout")
    isVis: Optional[Union[bool, str]] = Field(None, title="visibility")
    limit: Optional[str] = Field(None, title="limit")
    maxRetakes: Optional[Decimal] = Field(None, title="maxRetakes")
    prefLabel: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="preferred label")
    randomMaxDelay: Optional[str] = Field(None, title="randomMaxDelay")
    schedule: Optional[Union[Schedule, str]] = Field(None, title="Schedule")
    valueRequired: Optional[bool] = Field(None)
    variableName: Optional[str] = Field(None, title="variableName")
    
    

class Participant(Agent):
    
    subject_id: Optional[str] = Field(None)
    
    

class Protocol(CreativeWork):
    
    about: Optional[str] = Field(None)
    addProperties: Optional[List[AdditionalProperty]] = Field(default_factory=list, title="addProperties")
    allow: Optional[List[Thing]] = Field(default_factory=list, title="allow")
    altLabel: Optional[str] = Field(None, title="alternate label")
    associatedMedia: Optional[str] = Field(None, title="associatedMedia")
    compute: Optional[List[ComputeSpecification]] = Field(default_factory=list, title="computation")
    cronTable: Optional[str] = Field(None, title="cronTable")
    description: Optional[str] = Field(None)
    landingPage: Optional[Union[LandingPage, str]] = Field(None, title="Landing page content")
    messages: Optional[List[MessageSpecification]] = Field(default_factory=list, title="messages")
    order: Optional[List[Union[Activity, Field, str]]] = Field(default_factory=list, title="Order")
    overrideProperties: Optional[List[OverrideProperty]] = Field(default_factory=list, title="overrideProperties")
    prefLabel: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="preferred label")
    schemaVersion: Optional[str] = Field(None)
    shuffle: Optional[bool] = Field(None, title="Shuffle")
    ui: Optional[UI] = Field(None, title="UI")
    version: Optional[str] = Field(None)
    
    

class Response(CreativeWork):
    
    isAbout: Optional[Union[Activity, Field]] = Field(None, title="isAbout")
    ui: Optional[UI] = Field(None, title="UI")
    value: Optional[List[Union[Decimal, DontKnow, Skipped, StructuredValue, bool, str]]] = Field(default_factory=list, title="value")
    wasAttributedTo: Optional[Participant] = Field(None)
    
    

class ResponseActivity(CreativeWork):
    
    endedAtTime: Optional[datetime ] = Field(None)
    generated: Optional[str] = Field(None)
    inLanguage: Optional[List[Union[LangString, str]]] = Field(default_factory=list)
    startedAtTime: Optional[datetime ] = Field(None)
    used: Optional[List[str]] = Field(default_factory=list)
    wasAssociatedWith: Optional[SoftwareAgent] = Field(None)
    
    

class ResponseOption(ConfiguredBaseModel):
    
    choices: Optional[List[Union[Choice, str]]] = Field(default_factory=list, title="choices")
    datumType: Optional[str] = Field(None, title="datumType")
    maxValue: Optional[Union[float, int]] = Field(None)
    minValue: Optional[Union[float, int]] = Field(None)
    multipleChoice: Optional[bool] = Field(None, title="Multiple choice response expectation")
    unitOptions: Optional[List[UnitOption]] = Field(default_factory=list, title="unitOptions")
    valueType: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="The type of the response")
    
    

class Schedule(ConfiguredBaseModel):
    
    None
    
    

class Skipped(ConfiguredBaseModel):
    
    None
    
    

class SoftwareAgent(ConfiguredBaseModel):
    
    version: Optional[str] = Field(None)
    url: Optional[str] = Field(None)
    
    

class StructuredValue(ConfiguredBaseModel):
    
    None
    
    

class Thing(ConfiguredBaseModel):
    
    None
    
    

class TimedOut(ConfiguredBaseModel):
    
    None
    
    

class UI(ConfiguredBaseModel):
    
    order: Optional[List[Union[Activity, Field, str]]] = Field(default_factory=list, title="Order")
    addProperties: Optional[List[AdditionalProperty]] = Field(default_factory=list, title="addProperties")
    overrideProperties: Optional[List[OverrideProperty]] = Field(default_factory=list, title="overrideProperties")
    message: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="Message")
    shuffle: Optional[bool] = Field(None, title="Shuffle")
    inputType: Optional[str] = Field(None, title="inputType")
    readonlyValue: Optional[str] = Field(None)
    allow: Optional[List[Thing]] = Field(default_factory=list, title="allow")
    valueRequired: Optional[bool] = Field(None)
    
    

class UnitOption(ConfiguredBaseModel):
    
    prefLabel: Optional[List[Union[LangString, str]]] = Field(default_factory=list, title="preferred label")
    value: Optional[List[str]] = Field(default_factory=list, title="value")
    
    

class VideoObject(ConfiguredBaseModel):
    
    contentUrl: str = Field(...)
    inLanguage: Optional[List[Union[LangString, str]]] = Field(default_factory=list)
    
    


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
UI.model_rebuild()
UnitOption.model_rebuild()
VideoObject.model_rebuild()

