Python code to partly mimic the functionality of the Conquest Pacs system ( http://www.natura-ingenium.nl/dicom.html ).
Done by reverse engineering ( not using the source code of conquest ).

a/ indexer properties : read a dicom tree and build a sqlite database from this which conforms to the Conquest standard.
b/ use the conquest style dicom.sql to define the columns
c/ provide low level procedures to write and read to the database
d/ provide basic SCU and SCP functionality

No attempt made to mimic
full dicom functionality
lua scripting
image representation
