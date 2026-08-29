# ==========================================
# API Schemas
# ==========================================

from pydantic import BaseModel, Field


class Recommendation(BaseModel):
    movieId: int
    title: str
    score: float


class RecommendationResponse(BaseModel):
    userId: int
    recommendations: list[Recommendation]


class RecommendationRequest(BaseModel):
    userId: int = Field(
        ...,
        description="ID of the user"
    )

    n: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Number of recommendations"
    )


# ==========================================
# Movie Schema
# ==========================================

class MovieResponse(BaseModel):
    movieId: int
    title: str