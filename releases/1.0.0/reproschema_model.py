from __future__ import annotations

import re
import sys
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic.version import VERSION as PYDANTIC_VERSION

if int(PYDANTIC_VERSION[0]) >= 2:
    from pydantic import BaseModel, ConfigDict, Field, field_validator
else:
    from pydantic import BaseModel, Field, validator
metamodel_version = "None"
version = "1.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        strict=False,
    )
    pass


class AllowedType(str, Enum):
    AllowAltResponse = "reproschema:AllowAltResponse"
    AllowExport = "reproschema:AllowExport"
    AllowReplay = "reproschema:AllowReplay"
    AllowSkip = "reproschema:AllowSkip"
    AutoAdvance = "reproschema:AutoAdvance"
    DisableBack = "reproschema:DisableBack"


class MissingType(str, Enum):
    Skipped = "reproschema:Skipped"
    DontKnow = "reproschema:DontKnow"
    Unknown = "reproschema:Unknown"
    TimedOut = "reproschema:TimedOut"


class Agent(ConfiguredBaseModel):
    pass


class Participant(Agent):
    """
    An Agent describing characteristics associated with a participant.
    """

    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    subject_id: Optional[str] = Field(None)


class Thing(ConfiguredBaseModel):
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class Activity(Thing):
    """
    An assessment in a protocol.
    """

    about: Optional[str] = Field(
        None, description="The subject matter of the Field."
    )
    altLabel: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="alternate label",
        description="The alternate label.",
    )
    associatedMedia: Optional[str] = Field(
        None,
        title="associatedMedia",
        description="A media object that encodes this creative work. This property is a synonym for encoding.",
    )
    citation: Optional[Dict[str, str]] = Field(default_factory=dict)
    compute: Optional[List[ComputeSpecification]] = Field(
        default_factory=list,
        title="computation",
        description="An array of objects indicating computations in an activity or protocol and maps it to the corresponding Item. scoring logic is a subset of all computations that could be performed and not all computations will be scoring. For example, one may want to do conversion from one unit to another.",
    )
    cronTable: Optional[str] = Field(None, title="cronTable")
    description: Optional[Dict[str, str]] = Field(default_factory=dict)
    image: Optional[Union[ImageObject, str]] = Field(
        None,
        title="image",
        description='An image of the item. This can be a <a class="localLink" href="http://schema.org/URL">URL</a> or a fully described <a class="localLink" href="http://schema.org/ImageObject">ImageObject</a>.',
    )
    isProprietary: Optional[bool] = Field(None)
    messages: Optional[List[MessageSpecification]] = Field(
        default_factory=list,
        title="messages",
        description="An array of objects to define conditional messages in an activity or protocol.",
    )
    preamble: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="Preamble",
        description="The preamble for an assessment.",
    )
    prefLabel: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="preferred label",
        description="The preferred label.",
    )
    schemaVersion: Optional[str] = Field(None)
    ui: Optional[UI] = Field(
        None,
        title="UI",
        description="An element to control UI specifications. Originally @nest in jsonld, but using a class in the model.",
    )
    version: Optional[str] = Field(None)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class AdditionalNoteObj(Thing):
    """
    A set of objects to define notes in a Item. For example, most Redcap and NDA data dictionaries have notes for each item which needs to be captured in reproschema
    """

    column: Optional[str] = Field(
        None,
        title="column",
        description="An element to define the column name where the note was taken from.",
    )
    source: Optional[str] = Field(
        None,
        title="source",
        description="An element to define the source (eg. RedCap, NDA) where the note was taken from.",
    )
    value: Optional[
        Union[
            Dict[str, str], MissingType, StructuredValue, bool, float, int, str
        ]
    ] = Field(
        None,
        title="value",
        description="The value for each option in choices or in additionalNotesObj",
    )
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class AdditionalProperty(Thing):
    """
    An object to describe the various properties added to assessments and Items.
    """

    allow: Optional[List[AllowedType]] = Field(
        default_factory=list,
        title="allow",
        description="An array of items indicating properties allowed on an activity or protocol.",
    )
    isAbout: Optional[Union[Activity, Item, str]] = Field(
        None,
        title="isAbout",
        description="A pointer to the node describing the item.",
    )
    isVis: Optional[Union[bool, str]] = Field(
        None,
        title="visibility",
        description="An element to describe (by boolean or conditional statement) visibility conditions of items in an assessment.",
    )
    limit: Optional[str] = Field(
        None,
        title="limit",
        description="An element to limit the duration (uses ISO 8601) this activity is allowed to be completed by once activity is available.",
    )
    maxRetakes: Optional[int] = Field(
        None,
        title="maxRetakes",
        description="Defines number of times the item is allowed to be redone.",
    )
    prefLabel: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="preferred label",
        description="The preferred label.",
    )
    randomMaxDelay: Optional[str] = Field(
        None,
        title="randomMaxDelay",
        description="Present activity/item within some random offset of activity available time up to the maximum specified by this ISO 8601 duration",
    )
    schedule: Optional[str] = Field(
        None,
        title="Schedule",
        description="An element to set make activity available/repeat info using ISO 8601 repeating interval format.",
    )
    valueRequired: Optional[bool] = Field(None)
    variableName: Optional[str] = Field(
        None,
        title="variableName",
        description="The name used to represent an item.",
    )
    ui: Optional[UI] = Field(
        None,
        title="UI",
        description="An element to control UI specifications. Originally @nest in jsonld, but using a class in the model.",
    )
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class Choice(Thing):
    """
    An object to describe a response option.
    """

    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    image: Optional[Union[ImageObject, str]] = Field(
        None,
        title="image",
        description='An image of the item. This can be a <a class="localLink" href="http://schema.org/URL">URL</a> or a fully described <a class="localLink" href="http://schema.org/ImageObject">ImageObject</a>.',
    )
    value: Optional[
        Union[
            Dict[str, str], MissingType, StructuredValue, bool, float, int, str
        ]
    ] = Field(
        None,
        title="value",
        description="The value for each option in choices or in additionalNotesObj",
    )
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class ComputeSpecification(Thing):
    """
    An object to define computations in an activity or protocol.
    """

    jsExpression: Optional[str] = Field(
        None,
        title="JavaScript Expression",
        description="A JavaScript expression for computations. A JavaScript expression to compute a score from other variables.",
    )
    variableName: Optional[str] = Field(
        None,
        title="variableName",
        description="The name used to represent an item.",
    )
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class Item(Thing):
    """
    An item in an assessment.
    """

    about: Optional[str] = Field(
        None, description="The subject matter of the Field."
    )
    additionalNotesObj: Optional[List[AdditionalNoteObj]] = Field(
        default_factory=list,
        title="additional notes",
        description="A set of objects to define notes in a field. For example, most Redcap and NDA data dictionaries have notes for each item which needs to be captured in reproschema.",
    )
    altLabel: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="alternate label",
        description="The alternate label.",
    )
    associatedMedia: Optional[str] = Field(
        None,
        title="associatedMedia",
        description="A media object that encodes this creative work. This property is a synonym for encoding.",
    )
    audio: Optional[Union[AudioObject, str]] = Field(
        None, title="audio", description="An audio object."
    )
    description: Optional[Dict[str, str]] = Field(default_factory=dict)
    image: Optional[Union[ImageObject, str]] = Field(
        None,
        title="image",
        description='An image of the item. This can be a <a class="localLink" href="http://schema.org/URL">URL</a> or a fully described <a class="localLink" href="http://schema.org/ImageObject">ImageObject</a>.',
    )
    isPartOf: Optional[Activity] = Field(None)
    preamble: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="Preamble",
        description="The preamble for an assessment.",
    )
    prefLabel: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="preferred label",
        description="The preferred label.",
    )
    question: Optional[Dict[str, str]] = Field(default_factory=dict)
    responseOptions: Optional[Union[ResponseOption, str]] = Field(
        None,
        title="Response options",
        description="An element (object or by URL)to describe the properties of response of the Item.",
    )
    schemaVersion: Optional[str] = Field(None)
    ui: Optional[UI] = Field(
        None,
        title="UI",
        description="An element to control UI specifications. Originally @nest in jsonld, but using a class in the model.",
    )
    version: Optional[str] = Field(None)
    video: Optional[Union[VideoObject, str]] = Field(None)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class LandingPage(Thing):
    """
    An object to define the landing page of a protocol.
    """

    inLanguage: Optional[str] = Field(None)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class MediaObject(Thing):
    """
    A media object, such as an image, video, audio, or text object embedded in a web page or a downloadable dataset.
    """

    inLanguage: Optional[str] = Field(None)
    contentUrl: str = Field(...)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class AudioObject(MediaObject):
    inLanguage: Optional[str] = Field(None)
    contentUrl: str = Field(...)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class ImageObject(MediaObject):
    inLanguage: Optional[str] = Field(None)
    contentUrl: str = Field(...)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class MessageSpecification(Thing):
    """
    An object to define messages in an activity or protocol.
    """

    jsExpression: Optional[str] = Field(
        None,
        title="JavaScript Expression",
        description="A JavaScript expression for computations. A JavaScript expression to compute a score from other variables.",
    )
    message: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="Message",
        description="The message to be conditionally displayed for an item.",
    )
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class OverrideProperty(Thing):
    """
    An object to override the various properties added to assessments and Items.
    """

    isAbout: Optional[Union[Activity, Item, str]] = Field(
        None,
        title="isAbout",
        description="A pointer to the node describing the item.",
    )
    isVis: Optional[Union[bool, str]] = Field(
        None,
        title="visibility",
        description="An element to describe (by boolean or conditional statement) visibility conditions of items in an assessment.",
    )
    limit: Optional[str] = Field(
        None,
        title="limit",
        description="An element to limit the duration (uses ISO 8601) this activity is allowed to be completed by once activity is available.",
    )
    maxRetakes: Optional[int] = Field(
        None,
        title="maxRetakes",
        description="Defines number of times the item is allowed to be redone.",
    )
    prefLabel: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="preferred label",
        description="The preferred label.",
    )
    randomMaxDelay: Optional[str] = Field(
        None,
        title="randomMaxDelay",
        description="Present activity/item within some random offset of activity available time up to the maximum specified by this ISO 8601 duration",
    )
    schedule: Optional[str] = Field(
        None,
        title="Schedule",
        description="An element to set make activity available/repeat info using ISO 8601 repeating interval format.",
    )
    valueRequired: Optional[bool] = Field(None)
    variableName: Optional[str] = Field(
        None,
        title="variableName",
        description="The name used to represent an item.",
    )
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class Protocol(Thing):
    """
    A representation of a study which comprises one or more assessments.
    """

    about: Optional[str] = Field(
        None, description="The subject matter of the Field."
    )
    altLabel: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="alternate label",
        description="The alternate label.",
    )
    associatedMedia: Optional[str] = Field(
        None,
        title="associatedMedia",
        description="A media object that encodes this creative work. This property is a synonym for encoding.",
    )
    compute: Optional[List[ComputeSpecification]] = Field(
        default_factory=list,
        title="computation",
        description="An array of objects indicating computations in an activity or protocol and maps it to the corresponding Item. scoring logic is a subset of all computations that could be performed and not all computations will be scoring. For example, one may want to do conversion from one unit to another.",
    )
    cronTable: Optional[str] = Field(None, title="cronTable")
    description: Optional[Dict[str, str]] = Field(default_factory=dict)
    landingPage: Optional[List[Union[LandingPage, str]]] = Field(
        default_factory=list,
        title="Landing page content",
        description="An element (by URL) to point to the protocol readme or landing page.",
    )
    messages: Optional[List[MessageSpecification]] = Field(
        default_factory=list,
        title="messages",
        description="An array of objects to define conditional messages in an activity or protocol.",
    )
    preamble: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="Preamble",
        description="The preamble for an assessment.",
    )
    prefLabel: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="preferred label",
        description="The preferred label.",
    )
    schemaVersion: Optional[str] = Field(None)
    ui: Optional[UI] = Field(
        None,
        title="UI",
        description="An element to control UI specifications. Originally @nest in jsonld, but using a class in the model.",
    )
    version: Optional[str] = Field(None)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class Response(Thing):
    """
    Describes the response of an item.
    """

    isAbout: Optional[Union[Activity, Item, str]] = Field(
        None,
        title="isAbout",
        description="A pointer to the node describing the item.",
    )
    value: Optional[
        Union[
            Dict[str, str], MissingType, StructuredValue, bool, float, int, str
        ]
    ] = Field(
        None,
        title="value",
        description="The value for each option in choices or in additionalNotesObj",
    )
    wasAttributedTo: Optional[Participant] = Field(None)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class ResponseActivity(Thing):
    """
    Captures information about some action that took place. It also links to information (entities) that were used during the activity
    """

    endedAtTime: Optional[datetime] = Field(None)
    generated: Optional[str] = Field(None)
    inLanguage: Optional[str] = Field(None)
    startedAtTime: Optional[datetime] = Field(None)
    used: Optional[List[str]] = Field(default_factory=list)
    wasAssociatedWith: Optional[SoftwareAgent] = Field(None)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class ResponseOption(Thing):
    """
    An element (object or by URL)to describe the properties of response of the Item.
    """

    choices: Optional[List[Union[Choice, str]]] = Field(
        default_factory=list,
        title="choices",
        description="An array to list the available options for response of the Item.",
    )
    datumType: Optional[str] = Field(
        None,
        title="datumType",
        description="Indicates what type of datum the response is (e.g. range,count,scalar etc.) for the Item.",
    )
    maxValue: Optional[Union[float, int]] = Field(None)
    minValue: Optional[Union[float, int]] = Field(None)
    multipleChoice: Optional[bool] = Field(
        None,
        title="Multiple choice response expectation",
        description="Indicates (by bool) if response for the Item has one or more answer.",
    )
    unitOptions: Optional[List[UnitOption]] = Field(
        default_factory=list,
        title="unitOptions",
        description="A list of objects to represent a human displayable name alongside the more formal value for units.",
    )
    valueType: Optional[List[str]] = Field(
        default_factory=list,
        title="The type of the response",
        description="The type of the response of an item. For example, string, integer, etc.",
    )
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class SoftwareAgent(Thing):
    """
    Captures information about some action that took place. It also links to information (entities) that were used during the activity
    """

    version: Optional[str] = Field(None)
    url: Optional[str] = Field(None)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class StructuredValue(Thing):
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class UI(ConfiguredBaseModel):
    """
    A group of properties related to UI.
    """

    order: Optional[List[Union[Activity, Item, str]]] = Field(
        default_factory=list,
        title="Order",
        description="An ordered list to describe the order in which the items of an assessment or protocol appear in the user interface.",
    )
    addProperties: Optional[List[AdditionalProperty]] = Field(
        default_factory=list,
        title="addProperties",
        description="An array of objects to describe the various properties added to assessments and Items.",
    )
    overrideProperties: Optional[List[OverrideProperty]] = Field(
        default_factory=list,
        title="overrideProperties",
        description="An array of objects to override the various properties added to assessments and fields.",
    )
    shuffle: Optional[bool] = Field(
        None,
        title="Shuffle",
        description="An element (bool) to determine if the list of items is shuffled or in order.",
    )
    allow: Optional[List[AllowedType]] = Field(
        default_factory=list,
        title="allow",
        description="An array of items indicating properties allowed on an activity or protocol.",
    )
    inputType: Optional[str] = Field(
        None,
        title="inputType",
        description="An element to describe the input type of a Item.",
    )
    readonlyValue: Optional[bool] = Field(None)


class UnitOption(Thing):
    """
    An object to represent a human displayable name alongside the more formal value for units.
    """

    prefLabel: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        title="preferred label",
        description="The preferred label.",
    )
    value: Optional[Union[Dict[str, str], str]] = Field(
        None,
        title="value",
        description="The value for each option in choices or in additionalNotesObj",
    )
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


class VideoObject(MediaObject):
    inLanguage: Optional[str] = Field(None)
    contentUrl: str = Field(...)
    id: Optional[str] = Field(
        None,
        description="A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI.",
    )
    name: Optional[Dict[str, str]] = Field(default_factory=dict)
    category: Optional[str] = Field(
        None,
        description="Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In an RDF database it should be a model class URI. This field is multi-valued.",
    )


Agent.model_rebuild()
Participant.model_rebuild()
Thing.model_rebuild()
Activity.model_rebuild()
AdditionalNoteObj.model_rebuild()
AdditionalProperty.model_rebuild()
Choice.model_rebuild()
ComputeSpecification.model_rebuild()
Item.model_rebuild()
LandingPage.model_rebuild()
MediaObject.model_rebuild()
AudioObject.model_rebuild()
ImageObject.model_rebuild()
MessageSpecification.model_rebuild()
OverrideProperty.model_rebuild()
Protocol.model_rebuild()
Response.model_rebuild()
ResponseActivity.model_rebuild()
ResponseOption.model_rebuild()
SoftwareAgent.model_rebuild()
StructuredValue.model_rebuild()
UI.model_rebuild()
UnitOption.model_rebuild()
VideoObject.model_rebuild()
