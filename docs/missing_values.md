# Missing-value reporting

Do not leave required metadata fields blank. If a value is absent, report why it is absent using a repository-approved missing-value term.

Repository-specific rules take priority. For INSDC submissions, use INSDC-accepted missing-value reporting terms where applicable.


|Phrase |Reason for use |When does it apply |INSDC token |DataCite code |ISO/GML (nilReason)|Definition|
|-------|---------------|-------------------|------------|--------------|-------|----------|
|not applicable; <br> not relevant |Field is outside the scope of the experiment |Depth for human stool sample |**not applicable** <br> for a control **missing: control sample** |**:unap**|**inapplicable**|Information is inappropriate to report; sometimes shows a gap in the standard itself.|
|not available|Value exists somewhere, but you cannot obtain it|Host BMI missing from a 1990 gut study| Top level: **missing** <br> or: **missing: third party data**| **:unav** | **missing**|Information of an expected format was not given because it is unavailable or unretrievable, with no expectation of later supply.|
|not recorded |Measurement was never captured|Ambient temperature not recorded during environmental swabbing| **missing: not collected** <br> **missing: lab stock** | **:unav**| **missing**|Information was expected but never collected at source.|
|not provided |Value exists but is under embargo / pending| Exact collection date withheld until publication of the clinical trial| **not provided**| **:tba**| **template** <br> or **other:pending**|Information of an expected format was not given now, but will be supplied later.|
|restricted access|Value exists but must remain confidential| Coordinates of endangered species or patient postcode that could be used to identify individual| **restricted access** | **:unal** <br> or **:unac** if the restriction is temporary | **withheld**|Information exists but cannot be released openly because of privacy, conservation or legal constraints.|

Sources: <br>
[INSDC Missing Value Reporting Terms](https://www.insdc.org/technical-specifications/missing-value-reporting/); <br>
[DataCite - Appendix 3: Standard values for unknown information](https://datacite-metadata-schema.readthedocs.io/en/4.6/appendices/appendix-3/#appendix-3-standard-values-for-unknown-information); <br>
[ISO 19115-3](https://schemas.isotc211.org/19115/-3/gco/1.0/gco/) <br>

## Practical rule

Use the most specific explanation available. `not collected` and `restricted access` mean different things and should not be collapsed into a generic `NA`.
