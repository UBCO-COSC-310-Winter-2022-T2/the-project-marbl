import sys 
print(f"PATH:::::::{sys.path}")
sys.path.append("c:\\Users\\Levi\\Desktop\\COSC310\\the-project-marbl\\clack_root") 
from front_end.User import User, UserList

def test_create_list():
    m = UserList()
    assert len(m) == 0
    assert m != None

def test_apend():
    m = UserList()
    u = User('bob','123','g@yolo')
    m.append(u)
    assert len(m) == 1
    m.append(u)
    assert len(m) == 2

def test_remove():
    m = UserList()
    u = User('bob','123','g@yolo')
    m.append(u)
    assert len(m) == 1
    m.remove(u)
    assert len(m) == 0

def test_insert():
    m = UserList()
    u = User('bob','123','g@yolo')
    m.append(u)
    m.insert(0,u)
    assert m[0] == u    
