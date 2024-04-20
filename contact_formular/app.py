from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# HTML template for the contact page
contact_form_template = "contact.html"

# Define a route for the contact form page
@app.get("/contact/", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse(contact_form_template, {"request": request})

# Define a route for handling form submission
@app.post("/contact/")
async def contact_form_post(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    # Here you can do whatever you want with the form data, like sending an email, saving it to a database, etc.
    # For now, let's just print the received data
    print(f"Received message from: {name}, Email: {email}, Message: {message}")
    
    # You can return a response if needed
    return {"message": "Message received successfully!"}
