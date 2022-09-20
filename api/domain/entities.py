from slugify import slugify
from typing import Optional
from pydantic import validator
from sqlmodel import SQLModel


class CourseBase(SQLModel):
    title: str
    description: Optional[str] = None

    @validator("slug", check_fields=False)
    def slugify(cls, v):
        return slugify(v)


class CourseCreate(CourseBase):
    pass


class CourseRead(CourseBase):
    slug: str


class CourseUpdate(CourseRead):
    pass
