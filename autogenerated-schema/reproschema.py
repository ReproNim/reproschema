from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, ConfigDict, Field
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


class AdditionalNoteObj(ConfiguredBaseModel):
    
    column: Optional[LangString] = Field(None, title="column")
    source: Optional[LangString] = Field(None, title="source")
    value: Optional[Union[Decimal, StructuredValue, bool, str]] = Field(None, title="value")
    

class AdditionalProperty(ConfiguredBaseModel):
    
    isAbout: Optional[Union[Activity, Field]] = Field(None, title="isAbout")
    isVis: Optional[Union[bool, str]] = Field(None, title="visibility")
    limit: Optional[str] = Field(None, title="limit")
    maxRetakes: Optional[Decimal] = Field(None, title="maxRetakes")
    prefLabel: Optional[str] = Field(None, title="preferred label")
    randomMaxDelay: Optional[str] = Field(None, title="randomMaxDelay")
    schedule: Optional[Union[Schedule, str]] = Field(None, title="Schedule")
    valueRequired: Optional[str] = Field(None)
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
    
    name: Optional[str] = Field(None)
    image: Optional[str] = Field(None, title="image")
    value_from_schema: Optional[Union[DontKnow, Skipped]] = Field(None)
    

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
    messages: Optional[List[MessageSpecification]] = Field(default_factory=list, title="messages")
    order: Optional[List[Union[Activity, Field, str]]] = Field(default_factory=list, title="Order")
    overrideProperties: Optional[List[OverrideProperty]] = Field(default_factory=list, title="overrideProperties")
    preamble: Optional[Union[LangString, str]] = Field(None, title="Preamble")
    prefLabel: Optional[str] = Field(None, title="preferred label")
    schemaVersion: Optional[str] = Field(None)
    shuffle: Optional[bool] = Field(None, title="Shuffle")
    version: Optional[str] = Field(None)
    

class DisableBack(ConfiguredBaseModel):
    
    None
    

class DontKnow(ConfiguredBaseModel):
    
    None
    

class Field(CreativeWork):
    
    about: Optional[str] = Field(None)
    additionalNotesObj: Optional[AdditionalNoteObj] = Field(None, title="additional notes")
    altLabel: Optional[str] = Field(None, title="alternate label")
    associatedMedia: Optional[str] = Field(None, title="associatedMedia")
    description: Optional[str] = Field(None)
    image: Optional[str] = Field(None, title="image")
    inputType: Optional[str] = Field(None, title="inputType")
    isPartOf: Optional[Activity] = Field(None)
    preamble: Optional[Union[LangString, str]] = Field(None, title="Preamble")
    prefLabel: Optional[str] = Field(None, title="preferred label")
    question: Optional[str] = Field(None)
    readonlyValue: Optional[str] = Field(None)
    responseOptions: Optional[Union[ResponseOption, str]] = Field(None, title="Response options")
    schemaVersion: Optional[str] = Field(None)
    version: Optional[str] = Field(None)
    

class LangString(ConfiguredBaseModel):
    
    None
    

class MessageSpecification(ConfiguredBaseModel):
    
    jsExpression: Optional[Union[bool, str]] = Field(None, title="JavaScript Expression")
    message: Optional[Union[LangString, str]] = Field(None, title="Message")
    

class OverrideProperty(ConfiguredBaseModel):
    
    isAbout: Optional[Union[Activity, Field]] = Field(None, title="isAbout")
    isVis: Optional[Union[bool, str]] = Field(None, title="visibility")
    limit: Optional[str] = Field(None, title="limit")
    maxRetakes: Optional[Decimal] = Field(None, title="maxRetakes")
    prefLabel: Optional[str] = Field(None, title="preferred label")
    randomMaxDelay: Optional[str] = Field(None, title="randomMaxDelay")
    schedule: Optional[Union[Schedule, str]] = Field(None, title="Schedule")
    valueRequired: Optional[str] = Field(None)
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
    landingPage: Optional[str] = Field(None, title="Landing page content")
    messages: Optional[List[MessageSpecification]] = Field(default_factory=list, title="messages")
    order: Optional[List[Union[Activity, Field, str]]] = Field(default_factory=list, title="Order")
    overrideProperties: Optional[List[OverrideProperty]] = Field(default_factory=list, title="overrideProperties")
    prefLabel: Optional[str] = Field(None, title="preferred label")
    schemaVersion: Optional[str] = Field(None)
    shuffle: Optional[bool] = Field(None, title="Shuffle")
    version: Optional[str] = Field(None)
    

class Response(CreativeWork):
    
    isAbout: Optional[Union[Activity, Field]] = Field(None, title="isAbout")
    value_from_schema: Optional[Union[Decimal, DontKnow, Skipped, StructuredValue, bool, str]] = Field(None)
    wasAttributedTo: Optional[Participant] = Field(None)
    

class ResponseActivity(CreativeWork):
    
    endedAtTime: Optional[str] = Field(None)
    generated: Optional[str] = Field(None)
    inLanguage: Optional[str] = Field(None)
    startedAtTime: Optional[str] = Field(None)
    used: Optional[str] = Field(None)
    

class ResponseOption(ConfiguredBaseModel):
    
    choices: Optional[List[Union[Choice, str]]] = Field(default_factory=list, title="choices")
    datumType: Optional[str] = Field(None, title="datumType")
    maxValue: Optional[str] = Field(None)
    minValue: Optional[str] = Field(None)
    multipleChoice: Optional[bool] = Field(None, title="Multiple choice response expectation")
    unitOptions: Optional[List[UnitOption]] = Field(default_factory=list, title="unitOptions")
    valueType: Optional[Union[LangString, str]] = Field(None, title="The type of the response")
    

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
    

class UnitOption(ConfiguredBaseModel):
    
    prefLabel: Optional[str] = Field(None, title="preferred label")
    value: Optional[str] = Field(None, title="value")
    


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
LangString.model_rebuild()
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
UnitOption.model_rebuild()

