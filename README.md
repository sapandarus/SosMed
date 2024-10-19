# SosMed

## As a user I can register to the platform

## As a user I can post an image that will be shown to the whole world

## As a user I can follow a person

## As a user I can unfollow a person

## As a user I can hide who I follow

## As a user I can see images that person that I follow post

Database

users

id                  text (uuid, pk)
name                text
username            text (index, unique)
email               text
phone_number        text
password            text
is_verified         bool
is_deleted          bool
created_at          timestamp
updated_at          timestamp
deleted_at          timestamp

posts

id                  text (uuid, pk)
user_id             text (uuid)
image               text (link)
created_at          timestamp
update_at           timestamp
deleted_at          timestamp

relation

user_id             text (uuid)
follower_user_id    text (uuid)
created_at          timestamp
is_deleted          bool
is_hidden           bool
created_at          timestamp
update_at           timestamp
deleted_at          timestamp