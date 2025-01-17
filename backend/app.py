from flask import Flask
from flask_cors import CORS
from routes.chat import chat_blueprint
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# Sentry points
sentry_sdk.init(
    dsn="https://f701bcfbc17102215093e6b1d0db2fb4@o4508588117262336.ingest.us.sentry.io/4508588119949312",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
)

def slow_function():
    import time
    time.sleep(0.1)
    return "done"

def fast_function():
    import time
    time.sleep(0.05)
    return "done"

# Manually call start_profiler and stop_profiler
# to profile the code in between
sentry_sdk.profiler.start_profiler()
for i in range(0, 10):
    slow_function()
    fast_function()
#
# Calls to stop_profiler are optional - if you don't stop the profiler, it will keep profiling
# your application until the process exits or stop_profiler is called.
sentry_sdk.profiler.stop_profiler()


# Initialize Flask app and configure CORS
app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(chat_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)