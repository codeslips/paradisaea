import os
import json
from os import walk, path
from utils import git as Git


def analysis_file_command(data):
   c = data['command']['quick']
   git_path = data['command']['git_path']
   cs = c.split('---')
   if len(cs) == 1:
      if cs[0] == 'push':
         Git.git_flow(cs[0],git_path)
   if len(cs) == 2:
      if cs[0] == 'git':
         Git.git_flow(cs[1],git_path)
      if cs[0] == 'new':
         data['filePath'] = data['filePath'] + cs[1]
         new_file(data)
      if cs[0] == 'note':
         data['filePath'] = "C:\\Users\\ASRS\\Desktop\\bamboo-note\\data\\" + cs[1] + ".html"
         new_file(data)
   return True

   

def change_file_content(data):
   if data["content"] != '' and os.path.exists(data['filePath']):
      #wait- os.path.getctime(path) judging file already changed
      fr=open(data['filePath'],"w",encoding="utf8")
      fr.write(data['content'])			
      fr.close()
      analysis_file_command(data)
      return True
   return False


def get_file_content(data):
   if os.path.exists(data['filePath']):
      fr=open(data['filePath'],errors='ignore',encoding="utf8").read()
      return fr
   return False


def new_file(data):
   if not os.path.exists(data['filePath']) and data['content'] == '':
      return new_blank_file(data)
   if not os.path.exists(data['filePath']) and data['content'] != '':
      return new_file_with_content(data)
   return False  

def new_blank_file(data):
   if not os.path.exists(data['filePath']):
      fr=open(data['filePath'],'w', encoding='utf-8')
      fr.close()
      return True
   return False   

def new_file_with_content(data):
   if not os.path.exists(data['filePath']):
      fr=open(data['filePath'],'w', encoding='utf-8')
      fr.write(data['content'])
      fr.close()
      return True
   return False   

def delete_exists_file(data):
   if os.path.exists(data['filePath']):
      os.remove(path)
      return True
   return False   


def get_folder_tree(data):
   return path_to_json(data['folderPath'])


def new_note_with_content(data):
   if request.method == 'GET' : return ""
   p = 'C:\\Users\\ASRS\\Desktop\\bamboo-note\\' + mes + '.html'
   if po == '':
   	Git.git_flow(mes,git_path)
   	return 'push ok'
   fr=open(p ,"w", encoding='utf-8')
   fr.write(po)  
   fr.close()  
   Git.git_flow(mes,git_path)
   return "create new note ok"  





def getFilesJson(hv):
	b=Bambooslips.objects.get(h_v=hv)
	bj=json.loads(b.b)
	return bj["json"]["files"]


def path_to_json(path):
	for i in exclude_folder_json(path):
		exclude_folder.append(i)
	return path_to_dict(path)

def exclude_folder_json(path):
	try:
		f = open(path+'bamboo-exclude.txt','r').read()
		fj = json.loads(f)
		if type(fj) == list:
			return fj
		else:
			return []
	except:
		return []


exclude_folder = ['node_modules']
depth = 3

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    d['depth'] = 0
    if os.path.isdir(path) and os.path.basename(path) not in exclude_folder and d['depth'] < 3:
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
        d['depth'] = d['depth'] + 1
    return d