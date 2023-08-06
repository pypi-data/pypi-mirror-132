# ReqIF

ReqIF is a Python library for working ReqIF format.

**The project is under construction.**

## Getting started

TBD

## Usage

### Passthrough command

TBD

### HTML dump

TBD

### Formatting ReqIF

TBD

## Implementation details

### Tolerance

The first-stage parser is made tolerant against possible issues in ReqIF.
It should be possible to parse a ReqIF file even if it is missing important
information. A separate validation command shall be used to confirm the validity
of the ReqIF contents.

## A bottom-up overview of the ReqIF format

- ReqIF is a standard. See reference document [RD01](#rd01-reqif-standard).
- ReqIF has a fixed structure (see "What is common for all ReqIF documents" 
below)
- ReqIF standard does not define a document structure for every documents so
a ReqIF tool implementor is free to choose between several implementation 
approaches. There is a
[ReqIF Implementation Guide](#rd02-reqif-implementation-guide)
that attempts to harmonize ReqIF tool developments. See also
"What is left open by the ReqIF standard" below.
- ReqIF files produced by various tool often have incomplete schemas. 

### What is common for all ReqIF documents

- All documents have ReqIF tags:
  - Document metadata is stored inside tags of `REQ-IF-HEADER` tag.
  - Requirements are stored as `<SPEC-OBJECT>`s
  - Requirements types are stored as `<SPEC-TYPE>`s
  - Supported data types are stored as `<DATATYPE>`
  - Relationships such as 'Parent-Child' as stored as `<SPEC-RELATIONS>`

### What is left open by the ReqIF standard
 
- How to distinguish requirements from headers/sections?
  - One way: create separate `SPEC-TYPES`: one or more for requirements and
    one for sections.
  - Another way: have one spec type but have it provide a `TYPE` field that can
  be used to distinguish between `REQUIREMENT` or `SECTION`.

## Reference documents

### [RD01] ReqIF standard

The latest version is 1.2:
[Requirements Interchange Format](https://www.omg.org/spec/ReqIF)

### [RD02] ReqIF Implementation Guide 

[ReqIF Implementation Guide](https://www.prostep.org/fileadmin/downloads/PSI_ImplementationGuide_ReqIF_V1-7.pdf)
