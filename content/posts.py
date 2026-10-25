"""New blog posts, in backlog order. Posts with a future date stay unpublished until a build on or after that date."""
from . import posts_infidelity, posts_alone, posts_restoration, posts_wives

NEW_POSTS = posts_infidelity.POSTS + posts_alone.POSTS + posts_restoration.POSTS + posts_wives.POSTS
