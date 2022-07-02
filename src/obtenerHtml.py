import re

channelTitleExpr = r'<channel>[\w\W]+?<title>([\w\W]+?)(?=<\/)'
channelDescriptionExpr = r'<channel>[\w\W]+?<description>([\w\W]+?)(?=<\/)'
channelLinkExpr = r'<channel>[\w\W]+?<link>([\w\W]+?)(?=<\/)'

itemsTitlesAndDescriptionExpr = r'<item>[\w\W]+?(<title>([\w\W]+?)(?=<\/)([\w\W]+?)<description>([\w\W]+?)(?=<\/)|<description>([\w\W]+?)(?=<\/)([\w\W]+?)<title>([\w\W]+?)(?=<\/))'

def exportarHtml(fileContent, pathFile):
  searchStr = '\\' if ("\\" in pathFile) else '/'
  rawFileName = pathFile.split(searchStr)[-1]
  fileName = rawFileName.split('.rss')[0]

  contentArr = []
  ctitle = f'<h1>{re.findall(channelTitleExpr, fileContent)[0].strip()}</h1>'
  cdescription = f'<p>{re.findall(channelDescriptionExpr, fileContent)[0].strip()}</p>'

  clinkContent = re.findall(channelLinkExpr, fileContent)[0].strip()
  clink = f'<a href="{clinkContent}">{clinkContent}</a>'
  
  # Base un archivo html
  contentArr.append(
    f'''<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset="utf-8">\n\t<title>{fileName}</title>\n</head>\n<body>'''
  )
  contentArr.extend([ctitle, cdescription, clink])

  matches = re.findall(itemsTitlesAndDescriptionExpr, fileContent)
  for match in matches:
    itemTitle = f'<h3>{match[1].strip()}</h3>'
    itemDescription = f'<p>{match[3].strip()}</p>'
    contentArr.extend([itemTitle, itemDescription])
  
  contentArr.append('\n</body>\n</html>')

  with open(f'{fileName}.html', 'w', encoding='UTF8') as f:
      for line in contentArr:
          f.write(line)
  f.close()
