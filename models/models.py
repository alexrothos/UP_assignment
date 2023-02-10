from app import db
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Company {}>'.format(self.name)

class CompanySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        include_relationships = True
        load_instance = True

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return '<Employee {}>'.format(self.name)

class EmployeeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        include_relationships = True
        load_instance = True

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return '<Product {}>'.format(self.name)

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_relationships = True
        load_instance = True