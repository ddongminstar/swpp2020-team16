import React, { Component } from 'react';
import PropTypes from 'prop-types';
import AceEditor from 'react-ace';
import raw from 'raw.macro';
import { withAlert } from 'react-alert';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import Button from '@material-ui/core/Button';
import 'ace-builds/src-noconflict/mode-python';
import 'ace-builds/src-noconflict/theme-monokai';

const isBrythonScriptLoaded = () => !!(
  document.getElementById('brython_sdk') &&
  document.getElementById('brython_stdlib')
);

const initBrython = () => window.brython();

const setBrythonEditorInputHandler = () => {
  // set editor input handler
  const parser = raw('./brython/codeEditorScript.script');
  const script = document.createElement('script');
  script.type = 'text/python3';
  script.text = parser;

  document.body.appendChild(script);
  return () => {
    document.body.removeChild(script);
  };
};

const onLoad = editor => editor;

class CodeIDEforHome extends Component {
  constructor(props) {
    super(props);
    this.state = {
      code: '#happy coding! fixedFunctionName required.',
    };
  }

  componentDidMount() {
    // after loading necessary brython scripts, inititate brython
    if (isBrythonScriptLoaded()) {
      window.addEventListener('load', initBrython);
    }
    setBrythonEditorInputHandler();
  }

  onSubmit = async () => {
    this.props.alert.show('You need to Login!');
  }

  render() {
    return (
      <Container>
        <Grid item xs={12}>
          <AceEditor
            name="ace-editor"
            mode="python"
            theme="monokai"
            height="500px"
            width="100%"
            onLoad={onLoad}
            onChange={newCode => this.setState({ code: newCode })}
            fontSize={14}
            showPrintMargin
            showGutter
            highlightActiveLine
            value={this.state.code}
            setOptions={{
              showLineNumbers: true,
              tabSize: 4,
            }}
          />
        </Grid>
        <Grid item xs={12}>
          <textarea
            id="console"
            readOnly
            style={{
              display: 'inline',
              backgroundColor: '#272822',
              color: 'white',
              width: `${100}%`,
              height: `${300}px`,
              padding: '1vw',
            }}
          />
        </Grid>
        <Grid container item xs={12}>
          <Grid item xs={6} align="center">
            <Button id="run" variant="outlined" size="large" color="secondary">
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RUN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </Button>
          </Grid>

          <Grid item xs={6} align="center">
            <Button
              id="submit"
              variant="outlined"
              size="large"
              color="primary"
              onClick={this.onSubmit}
            >
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SUBMIT&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </Button>
          </Grid>
          <textarea hidden id="code-pipe" value={this.state.code} onChange={() => { }} />
        </Grid>
      </Container>
    );
  }
}

CodeIDEforHome.propTypes = {
  alert: PropTypes.object.isRequired,
};

export default withAlert()(CodeIDEforHome);
