remark: package.json
	npx remark ./docs/*.md ./docs/**/*/md --rc-path .remarkrc

package.json:
	npm install `cat npm-requirements.txt`
