from ninja import Router
from datetime import date
from ninja import Schema,Router
from typing import List
from ..dbm import file as File


router = Router()

class FileIn(Schema):
   content: str = None
   filePath: str = None
   fileInfo: dict = None
   command: dict = None

class FileOut(Schema):
   content: str
   tips: str
   fileInfo: dict
   
   
class FolderIn(Schema):
   rootPath: str = None
   folderPath: str = None
   command: dict = None

class FolderOut(Schema):
   tips: str
   folderTree: dict  
   
@router.post("folder/tree/", response= FolderOut)
def get_folder_path_tree(request, payload:FolderIn):
    folder_tree = File.get_folder_tree(payload.dict())
    res = {'tips': 'error', 'folderTree': {}}
    if folder_tree:
       res['tips'] = 'success'
       res['folderTree'] = folder_tree
    return res

@router.get("/", response= FileOut)
def get_file_content(request, filePath: str):
    file_content = File.get_file_content({'filePath': filePath})
    res = {'tips': 'error', 'content': '', 'fileInfo': {}}
    if file_content:
       res['tips'] = 'success'
       res['content'] = file_content
    return res

@router.post("/", response= FileOut)
def new_file(request, payload:FileIn):
    file_change = File.new_file(payload.dict())
    res = {'tips': 'error', 'content': '', 'fileInfo': {}}
    if file_change:
       res['tips'] = 'success'
    return res


@router.post("command/", response= FileOut)
def new_file(request, payload:FileIn):
    file_change = File.analysis_file_command(payload.dict())
    res = {'tips': 'error', 'content': '', 'fileInfo': {}}
    if file_change:
       res['tips'] = 'success'
    return res

@router.put("/", response= FileOut)
def update_file_content(request, payload:FileIn):
    file_change = File.change_file_content(payload.dict())
    res = {'tips': 'error', 'content': '', 'fileInfo': {}}
    if file_change:
       res['tips'] = 'success'
    return res





'''
#@router.put("/bamboo/{open_id}")
def update_bamboo(request,open_id:int,payload:BambooOpenIn):
    bamboo = get_object_or_404(BambooOpenModel,open_id=open_id)
    for attr,value in payload.dict().items():
        setattr(bamboo,attr,value)
        bmaboo.save()
    return {"success": True}

#@router.delete("/bmaboo/{open_id}")
def delete_bmaboo(request,open_id: int):
    bamboo = get_object_or_404(BambooOpenModel,open_id=open_id)
    bamboo.delete()
    return {"success": True}
'''