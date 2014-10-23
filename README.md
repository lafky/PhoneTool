PhoneTool
=========

PhoneTool is an application that allows the user to rapidly search a SQLite database for contact information for individuals within an organization.  It is currently used at SLAC National Accelerator Laboratory.

The only four files required to use this are phonetool.py, ui_phonetool.py, ui_add.py, and names.db.  The .ui files are provided since the application was designed with Qt4 Designer, however they are not required.

When the application is launched it steals focus to the "name" search bar.  As the user begins typing, the string typed is automatically checked by a function against matching names in the database, and said names are displayed along with available contact info.  If the user checks the "make table editable" check box, any changes entered into the table (other than in the "name" field) will persist.  To add or remove entries the user must click the "Add/Update/Delete" button.  When adding an entry the only field required is the "name" field.
