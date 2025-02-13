from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required, current_user
import google.generativeai as palm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired
from tables import Post, User, db
import random

#Setting up AI api keys
palm.configure(api_key='')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
#print(model)


story_blueprint = Blueprint('story', __name__, template_folder='templates')
@story_blueprint.get("/story/")
@login_required
def get_story():
    story_form: StoryForm = StoryForm()
    return render_template("storyForm.html", form=story_form) #Change to new html input

@story_blueprint.post("/story/")
@login_required
def post_story():
    form: StoryForm = StoryForm()

    if form.validate():
        #Putting all of the user inputs into a list to easily add to a string
        nouns = [str(form.noun1.data), str(form.noun2.data), str(form.noun3.data), str(form.noun4.data), str(form.noun5.data)]
        verbs = [str(form.verb1.data), str(form.verb2.data), str(form.verb3.data), str(form.verb4.data)]
        adjectives = [str(form.adjective1.data), str(form.adjective2.data), str(form.adjective3.data)]

        #AI Story Generation
        prompt = """
Create a %s short story in using the words %s as nouns, %s as verbs,
and %s as adjectives. You can only use these words once in the story. 
Start the story by completing the phrase: "It is". The story must be close to five hundred words long and in three properly formatted paragraphs.
""" % (form.topic.data, " ".join(nouns), ' '.join(verbs), ' '.join(adjectives))

        story_completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=random.uniform(0.3,0.9),
        top_k = 40,
        # The maximum length of the response
        max_output_tokens=2000,
    )
        answer = story_completion.result
        
        prompt = """Create a title to the story of %s""" % (answer)
        #AI Title Creation
        title_completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=20
        )

        title = title_completion.result
        #Getting variables for adding story to database
        currUser = current_user.username #type: ignore
        userID = User.query.filter_by(username=currUser).first().id #type: ignore
        #Adding Story to database
        story = Post(post_title=title, post_story=answer, user_id=userID) #type: ignore
        db.session.add(story)
        db.session.commit()

        return redirect(f"/post/{story.id}")
    else:
        for field,error_msg in form.errors.items():
            flash(f"{field}: {error_msg}")
        return redirect(url_for("get_story"))

#Forms for user input
class StoryForm(FlaskForm):
    topic = SelectField('Select Topic of Story', choices=[('Western', 'Western'), ('Science Fiction', 'Science Fiction'), ('Modern', 'Modern'), ('Medieval', 'Medieval'), ('Fantasy', 'Fantasy')])
    noun1 = StringField("Enter Noun: ", validators=[InputRequired()])
    noun2 = StringField("")
    noun3 = StringField("")
    noun4 = StringField("")
    noun5 = StringField("")
    adjective1 = StringField("Enter Adjective: ", validators=[InputRequired()])
    adjective2 = StringField("")
    adjective3 = StringField("")
    verb1 = StringField("Enter Verb: ", validators=[InputRequired()])
    verb2 = StringField("")
    verb3 = StringField("")
    verb4 = StringField("")
    submit = SubmitField("Submit")