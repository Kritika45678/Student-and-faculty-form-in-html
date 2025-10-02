from lxml import etree

# Load DTD
with open("DTD.dtd", "r") as dtd_file:
    dtd_file= etree.DTD(dtd_file)

# Parse XML
xml_doc = etree.parse("XmlProgram.xml")

# Validate XML against DTD
if dtd_file.validate(xml_doc):
    print("XML is valid according to DTD ✅")
else:
    print("XML is NOT valid ❌")
    print(dtd.error_log.filter_from_errors())
