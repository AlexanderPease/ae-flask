import React from "react";
import { InputGroup, FormControl, Button } from "react-bootstrap";

var $ = require('jquery');

export default class NewsletterForm extends React.Component {
  constructor(props, context) {
    super(props, context);

    this.handleChange = this.handleChange.bind(this);
    this.submitForm = this.submitForm.bind(this);
    this.handleSuccess = this.handleSuccess.bind(this);

    this.state = {
      value: '',
      success: false
    };
  }

  handleChange(e) {
    this.setState({ value: e.target.value });
  }

  submitForm() {
    $.post(
      window.location.href + 'lead',
      {'email': this.state.value},
      (data) => {  
        if (data['code'] == 200) {
          this.handleSuccess();
        } else {
          // Potential future behavior
        }
      }
    );
  }

  handleSuccess() {
    this.setState({ success: true });
  }

  render() {
    return (
      <form>
        <h2>Let Me Know About Future Workshops</h2>
        <InputGroup>
          <FormControl
            type="text"
            value={this.state.value}
            className="form-negative"
            placeholder="example@email.com"
            onChange={this.handleChange}
            disabled={this.state.success}
          />
          <div className="input-group-append">
            <Button
              bsStyle="default"
              onClick={this.submitForm}
              disabled={this.state.success}
            >
              {this.state.success ? 'Submitted!' : 'Sign Up'}
            </Button>
          </div>
        </InputGroup>
      </form>
    );
  }
}