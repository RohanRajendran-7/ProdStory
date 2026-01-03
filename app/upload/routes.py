from flask import Blueprint, redirect, url_for, request
from app.process.transcription import transcribe_video
# The second argument is '__name__', which tells Flask where to find this blueprint
upload_bp = Blueprint('video', __name__)


@upload_bp.route('/videoregister')
def register():
    return "This is the success page."


@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        video = request.files.get('video')
        if video:
            # Save the file to a desired location
            video.save(f'/Users/rohanrajendran/Test/media/{video.filename}')
            transcribe_video(f'/Users/rohanrajendran/Test/media/{video.filename}')
            return redirect(url_for('video.register'))
        return "No file uploaded.", 400
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="video" accept="video/*">
            <button type="submit">Upload Video</button>
        </form>
    '''
@upload_bp.route('/view-uploads')
def view():
    return "This is the view page."
