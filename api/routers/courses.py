from typing import List
from settings import Settings, get_settings
from fastapi import APIRouter, Depends
from domain.entities import CourseRead
from data.repos import CourseRepository

router = APIRouter(
    tags=["Courses"],
    prefix="/courses",
)


@router.get("/")
def origem_normativo_lista(
    settings: Settings = Depends(get_settings),
) -> List[CourseRead]:
    repo: CourseRepository = settings.CourseRepository()
    return repo.read_all()
