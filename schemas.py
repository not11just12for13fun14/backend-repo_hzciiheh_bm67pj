"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import Optional, List

# Example schemas (you can keep or remove if not used):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Portfolio-focused schemas

class Project(BaseModel):
    """
    Portfolio projects
    Collection name: "project"
    """
    title: str = Field(..., description="Project title")
    description: str = Field(..., description="Short summary of the project")
    tech_stack: List[str] = Field(default_factory=list, description="Technologies used")
    repo_url: Optional[HttpUrl] = Field(None, description="Git repository URL")
    demo_url: Optional[HttpUrl] = Field(None, description="Live demo URL")
    image_url: Optional[HttpUrl] = Field(None, description="Cover image URL")

class Message(BaseModel):
    """
    Contact messages
    Collection name: "message"
    """
    name: str = Field(..., min_length=2, description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    subject: str = Field(..., min_length=2, description="Message subject")
    message: str = Field(..., min_length=5, max_length=5000, description="Message body")
