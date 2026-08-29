# ==========================================
# Movie Recommendation Engine
# ==========================================

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

from pathlib import Path
import json

import numpy as np
import polars as pl
from scipy.sparse import load_npz

import implicit
from implicit.cpu.als import AlternatingLeastSquares


# ==========================================
# Artifact Paths
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

MODEL_PATH = (
    ARTIFACTS_DIR
    / "model"
    / "als_model.npz"
)

USER_MAPPING_PATH = (
    ARTIFACTS_DIR
    / "mappings"
    / "user_to_index.json"
)

MOVIE_MAPPING_PATH = (
    ARTIFACTS_DIR
    / "mappings"
    / "movie_to_index.json"
)

MOVIE_IDS_PATH = (
    ARTIFACTS_DIR
    / "mappings"
    / "movie_ids.json"
)

USER_ITEMS_PATH = (
    ARTIFACTS_DIR
    / "data"
    / "user_items.npz"
)

MOVIE_METADATA_PATH = (
    ARTIFACTS_DIR
    / "metadata"
    / "movies.parquet"
)


# ==========================================
# Load Final ALS Model
# ==========================================

model = AlternatingLeastSquares.load(
    str(MODEL_PATH)
)


# ==========================================
# Load Mappings
# ==========================================

with open(
    USER_MAPPING_PATH,
    "r",
    encoding="utf-8"
) as file:

    user_to_index = {
        int(user_id): int(user_index)
        for user_id, user_index in json.load(file).items()
    }


with open(
    MOVIE_MAPPING_PATH,
    "r",
    encoding="utf-8"
) as file:

    movie_to_index = {
        int(movie_id): int(movie_index)
        for movie_id, movie_index in json.load(file).items()
    }


with open(
    MOVIE_IDS_PATH,
    "r",
    encoding="utf-8"
) as file:

    movie_ids = np.asarray(
        json.load(file),
        dtype=np.int64
    )


# ==========================================
# Load User-Item Matrix
# ==========================================

user_items = load_npz(
    USER_ITEMS_PATH
).tocsr()


# ==========================================
# Load Movie Metadata
# ==========================================

movie_metadata = (
    pl.read_parquet(MOVIE_METADATA_PATH)
    .select(
        ["movieId", "title"]
    )
)


# ==========================================
# Build Movie Lookup
# ==========================================

movie_lookup = {
    int(row["movieId"]): row["title"]
    for row in movie_metadata.iter_rows(
        named=True
    )
}


# ==========================================
# Recommendation Function
# ==========================================

def recommend_movies(
    user_id: int,
    n: int = 10
) -> list[dict]:

    if user_id not in user_to_index:
        raise ValueError(
            f"User {user_id} was not found."
        )

    if n < 1 or n > 100:
        raise ValueError(
            "n must be between 1 and 100."
        )

    user_index = user_to_index[user_id]

    recommendations, scores = model.recommend(
        userid=np.array(
            [user_index],
            dtype=np.int32
        ),
        user_items=user_items[user_index],
        N=n,
        filter_already_liked_items=True
    )

    results = []

    for movie_index, score in zip(
        recommendations[0],
        scores[0]
    ):

        movie_id = int(
            movie_ids[movie_index]
        )

        results.append(
            {
                "movieId": movie_id,
                "title": movie_lookup.get(
                    movie_id,
                    "Unknown"
                ),
                "score": float(score)
            }
        )

    return results


# ==========================================
# Movie Lookup
# ==========================================

def get_movie(movie_id: int) -> dict:

    if movie_id not in movie_lookup:
        raise ValueError(
            f"Movie {movie_id} was not found."
        )

    return {
        "movieId": movie_id,
        "title": movie_lookup[movie_id],
    }