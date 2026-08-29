# ==========================================
# Movie Recommendation API
# ==========================================

from fastapi import FastAPI, HTTPException

from api.recommender import (
    recommend_movies,
    get_movie,
)
from api.schemas import (
    RecommendationRequest,
    RecommendationResponse,
    MovieResponse,
)



# ==========================================
# FastAPI Application
# ==========================================

app = FastAPI(
    title="Movie Recommendation API",
    description="Personalized movie recommendations using ALS.",
    version="1.0.0",
)


## ==========================================
# Health Check
# ==========================================

@app.get("/")
def root():
    return {
        "message": "Movie Recommendation API is running."
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# ==========================================
# Recommendation Endpoint
# ==========================================

@app.post(
    "/recommend",
    response_model=RecommendationResponse,
)
def get_recommendations(
    request: RecommendationRequest,
):

    try:

        recommendations = recommend_movies(
            user_id=request.userId,
            n=request.n,
        )

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error),
        )

    return RecommendationResponse(
        userId=request.userId,
        recommendations=recommendations,
    )


# ==========================================
# Movie Information Endpoint
# ==========================================

@app.get(
    "/movie/{movie_id}",
    response_model=MovieResponse,
)
def get_movie_info(movie_id: int):

    try:

        movie = get_movie(movie_id)

    except ValueError as error:

        raise HTTPException(
            status_code=404,
            detail=str(error),
        )

    return movie