from fastapi import FastAPI

app = FastAPI()

@app.get('/', tags=['ROOT'])
async def root()->dict:
    return{"Hello": "world"}



@app.get('/todos', tags=['tasks'])
async def get_todo() ->dict:
    return{"data": todos}


@app.post('/todos', tags=['tasks'])
async def create_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": "A task has been created successfully"
        }

@app.put('/todos/{id}', tags=['tasks'])
async def update_todo(id:int, body:dict) -> dict:
    for task in todos:
        if int((['id'])) == id:
            task['Task'] = body['Task']
            return {
                "data": f"Task with id {id} has been updated successfully"
                }
        return {
            "data": f"Task with id {id} was not found in our database"
        }

@app.delete('/todos/{id}', tags=['tasks'])
async def delete_todo(id: int) -> dict:
    for task in todos:
        if int(task['id']) == id:
            todos.remove(task)
            return {
                "data": f"Task with id {id} has been Removed from the list of tasks"
                }
        return {
            "data": f"Task with id {id} was not found in our database"
            }

todos = [
            {
            "id": "1",
            "Task": "Create a project"
            },
            {
            "id": "2",
            "Task": "Deliver a project"
            }
        ]



