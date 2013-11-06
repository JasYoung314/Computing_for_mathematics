#! /usr/bin/env python

import os

# Open index file

index_file = open("../index.md", "w")
index_file.write("# Computing for mathematics")
index_file.write("\n")

# Notes

index_file.write("""
This website contains the lab sheets for the first term of Computing for Mathematics. Each lab sheet contains links to a number of videos that should help with the exercises.
                 """)
index_file.write("\n")

# Write course notes

target_dir = "../LabSheets"

list_of_lab_sheets = os.listdir(target_dir)
list_of_md_sheets = [p for p in list_of_lab_sheets if p[-3:] == ".md"]
list_of_md_sheets.sort()
number_of_lab_sheets = len(list_of_md_sheets)
print "%s lab sheets read." % number_of_lab_sheets

index_file.write("\n")
index_file.write("\n## Lab Sheets")
index_file.write("\n")

for i in range(len(list_of_md_sheets)):
    outfile = open(target_dir + "/" + list_of_md_sheets[i])
    data = outfile.read().split("\n")
    outfile.close()
    file_name = list_of_md_sheets[i][:-3]
    index_file.write("\n%s. Lab Sheets %s: %s" % (i + 1, i + 1, data[0][data[0].index("-") + 2:]))
    index_file.write("\n")
    index_file.write("\n\t[html (recommended)](./LabSheets/%s.html), [pdf](./LabSheets/%s.pdf), [docx](./LabSheets/%s.docx)" % (file_name, file_name, file_name))
    index_file.write("\n")

# Write handout

target_dir = "../Handouts"

list_of_handouts = os.listdir(target_dir)
list_of_md_sheets = [p for p in list_of_handouts if p[-3:] == ".md"]
list_of_md_sheets.sort()
number_of_lab_sheets = len(list_of_md_sheets)
print "%s handouts read." % number_of_lab_sheets

index_file.write("\n")
index_file.write("\n## Handouts")
index_file.write("\n")

for i in range(len(list_of_md_sheets)):
    outfile = open(target_dir + "/" + list_of_md_sheets[i])
    data = outfile.read().split("\n")
    outfile.close()
    file_name = list_of_md_sheets[i][:-3]
    index_file.write("\n%s. Handout %s: %s" % (i + 1, i + 1, data[0][data[0].index("-") + 2:]))
    index_file.write("\n")
    index_file.write("\n\t[html (recommended)](./Handouts/%s.html), [pdf](./Handouts/%s.pdf), [docx](./Handouts/%s.docx)" % (file_name, file_name, file_name))
    index_file.write("\n")
# Write Lesson plans

#target_dir = "../Lesson_Plans"
#index_file.write("\n## Lesson plans")
#
#list_of_plans = os.listdir(target_dir)
#list_of_plans = [p for p in list_of_plans if p[-3:] == ".md"]
#list_of_plans.sort()
#number_of_plans = len(list_of_plans)
#print "%s lesson plans read." % number_of_plans
#
#for i in range(len(list_of_plans)):
#    outfile = open(target_dir + "/" + list_of_plans[i])
#    data = outfile.read().split("\n")
#    outfile.close()
#
#    index_file.write("\n%s. Week %s: [%s](./Lesson_Plans/Week_%.02d.html)" % (i + 1, i + 1, data[1][2:], i + 1))
#
#index_file.write("\n")
#
#
#index_file.write("""

### Reading List

index_file.write("""
Alternative resources can be found [here](./alternativeresources.html).

[My personal website](http://www.vincent-knight.com/) contains information with regards to assessment and also solutions to the lab sheets.

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-38016329-2']);
  _gaq.push(['_setDomainName', 'github.com']);
  _gaq.push(['_setAllowLinker', true]);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
                 """)


index_file.close()

os.system("pandoc ../index.md -o ../index.html")
