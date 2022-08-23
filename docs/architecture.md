# Project architecture and tips

First of all, this project is designed by MVC architectural pattern.

## Routers
This is a Controller type of MVC. Responsible for receiving and transmitting data.

## Models
This is ad Model type of MVC. Data access layer and data layout in database

## Schemas
Pydantic models for serializing data.

## Database
Responsible for configure database connection and other settings.

## Services
All business logic located here.

## Core
Core application with settings.