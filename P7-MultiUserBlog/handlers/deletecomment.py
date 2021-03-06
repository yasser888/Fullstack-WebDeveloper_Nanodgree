# Models
from models.blog import Blog
from models.likes import Like
from models.unlikes import Unlike

from models.unlikes import Unlike

from models.comment import Comment

# Handlers
from handlers.bloghandler import Handler
from handlers.postpage import PostPage

from google.appengine.ext import db
from helpers import *
import time

# Define delete comment class-------------------------------------------------


class DeleteComment(Handler):
    @user_logged_in
    def get(self, post_id, comment_id):
        # get the comment from the comment id
        comment = Comment.get_by_id(int(comment_id))
        # check if there is a comment associated with that id
        if comment:
            # check if this user is the author of this comment
            if comment.user.name == self.user.name:
                # delete the comment and redirect to the post page
                db.delete(comment)
                time.sleep(0.1)
                self.redirect('/post/%s' % str(post_id))
            # otherwise if this user is not the author of this comment throw an
            # error
            else:
                self.write("You cannot delete other user's comments")
        # otherwise if there is no comment associated with that id throw an
        # error
        else:
            self.write("This comment no longer exists")
