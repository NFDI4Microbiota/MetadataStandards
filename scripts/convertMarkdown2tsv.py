#!/usr/bin/python3
#pk
import os, sys
import regex as re
import argparse

def parse_markdown_to_tsv(md_file,overwrite_existing=False):
	tsv_file = re.sub(r"[.]md$","",md_file)+".tsv"
	if not overwrite_existing and os.path.exists(tsv_file):
		print(f"SKIPPING {md_file} as the TSV file {tsv_file} is present (use -f to force overwriting)...") 

	category="NA"

	md_content=""
	with open(md_file, 'r', encoding='utf-8') as f:
		md_content = f.read()
	md_content = re.sub(r'[^\x00-\x7F]',' ', md_content) # remove emojis etc...
	md_content = md_content.replace(u'\xa0', u' ') # there are some weird non-breaking chars in the mds

	table=[]
	num_cols = -1
	is_first = True
	found_references = False
	last_line=""
	last_year=0
	last_firstauthor=""
	last_toolname=""
	reference_data = {}
	# seen = {}

	for line in md_content.split("\n"):
		if res := re.search(r"^##.* `(.*)`",line):
			category = res.group(1)
		if category == "NA":
			if res := re.search(r"^##.* for (.*)",line):
				category = res.group(1)
		if res := re.search(r"^[|].* [|] .* [|] *$",line):
			cols = re.split(r" *[|] *",line)
			cols = [ x if x != "" else "NA" for x in cols ] 
			cols = cols[1:len(cols)-1] # skip first and last
			cols = [ re.sub(r"[*]+","",x) for x in cols ] # remove md bold stuff

			# if "-".join(cols) in seen: # -> this can cause problems as some definitions are identical for different categories ...
			# 	continue
			# seen["-".join(cols)]=1

			if len(cols)<3: # skip lines with few entries
				continue
			if num_cols == -1:
				num_cols = len(cols)
			if len(cols) != num_cols: # sanity check if the table makes sense
				if len(cols) > num_cols:
					print(f" WARNING there are more columns present as announced in the header, I will truncate the line")
					cols=cols[0:num_cols-1]
				else:
					print(f" WARNING skipping line with inconcordant number of columns")
				continue

			if not is_first:
				cols = [category]+cols
			else:
				cols = ["category"]+cols

			table += [ cols ]
			is_first=False

		if re.search(r"# [Rr]eferences",line):
			found_references = True
		if found_references:
			if res := re.search(r"^<(htt.*)>[.]?",line):
				url = res.group(1)
				reference_data[ last_line ] = url
				reference_data[f"{last_firstauthor} {last_year}"] = url
				reference_data[f"{last_firstauthor} et al. {last_year}"] = url
				reference_data[f"{last_toolname}"] = url

				last_firstauthor=""
				last_year=""
				last_toolname=""

		if res := re.search(r"((20|19)[0-9]{2})",line):
			if int(res.group(1))>1500 and int(res.group(1))<2100:
				last_year=int(res.group(1))
		if last_line == "":
			last_firstauthor = re.sub(r"^([^ ,]+)[,].*$",r"\1",line)
			last_toolname = re.sub(r"^ ?([^.]+)[.] ?.*$",r"\1",line)
		
		last_line = re.sub(r"[.]$","",re.sub(r"[*]+","",re.sub(r"^ *| *$","",line)))

	# replace the references
	for rows in table:
		for res in re.finditer(r"[(] *([^()]*) *[)]",rows[len(rows)-1]):
			key = res.group(1).rstrip()
			if key in reference_data:
				url=reference_data[key]
				ref_url = reference_data[key]
				rows[len(rows)-1] = rows[len(rows)-1].replace(key,url)
				break

	# print stuff to tsv ...
	if len(table)>0:
		with open(tsv_file, 'w') as of:
			for rows in table:
				of.write("\t".join(rows)+"\n")
		print(f"Status {md_file} to {tsv_file} : OK") 

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description="Parse MD files for the repository MetadataStandards (https://github.com/NFDI4Microbiota/MetadataStandards/) into TSV format. Existing TSV files are NOT overwritten by default (they are skipped)",epilog="EXAMPLE: `python3 convertMarkdown2tsv.py -f Technical/*md`\nAUTHOR: Paul Klemm")
	parser.add_argument('files', nargs='+', help='List of MARKDOWN files to process, you can use "." to crawl to all subdirectories. Otherwise specify individual md files.')
	parser.add_argument("-f", "--force", action="store_true", help="overwrite existing tsv files")
	args = parser.parse_args()

	md_files = []

	if len(args.files) == 1 and args.files[0] == ".": # find all md files okok
		for root, dirs, files in os.walk("."):
			for file in files:
				if file.endswith('.md') and file not in ["CHANGELOG.md","CODE_OF_CONDUCT.md","NEXT_VERSION.md","README.md"]:
					md_files.append(os.path.join(root, file))
	else:
		md_files = [ x for x in args.files if x.endswith(".md") and os.path.exists(x) ]
	
	for file in md_files:
		parse_markdown_to_tsv(file,args.force)
