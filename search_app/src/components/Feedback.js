import React from 'react'
import { Formik } from 'formik'
import * as Yup from 'yup'
import { Form, Col, Button } from 'react-bootstrap'
import axios from 'axios'

const schema = Yup.object().shape({
  name: Yup.string().min(2, 'Too short').max(50, 'Too long').required('Required'),
  category: Yup.string(),
  subject: Yup.string().min(2, 'Too short').max(50, 'Too long').required('Required'),
  content: Yup.string().min(2, 'Too short').max(50000, 'Too long').required('Required'),
  email: Yup.string().email('Invalid email').required('Required')
});

const postFeedback = (formData) => {
  axios.post('/feedback', formData)
    .then(function (response) {
      alert(`Thank you for your feedback!\nticket #${response.data.ticket}`);
    })
    .catch(function (error) {
      console.log(error);
    });
};

const Feedback = () => (
  <div>
    <h3>Questions? Comments? Please let us know.</h3>
    <Formik
      validationSchema={schema}
      onSubmit={postFeedback}
      initialValues={{
        referrer: document.referrer,
        category: '',
        subject: '',
        content: '',
        name: '',
        email: ''
      }}
    >
      {({
        handleSubmit,
        handleChange,
        handleBlur,
        values,
        touched,
        isValid,
        errors
      }) => (
        <Form noValidate onSubmit={handleSubmit}>
          <Form.Row>
            <Form.Group as={Col} md="4" controlId="validationFormik01">
              <Form.Label>Name</Form.Label>
              <Form.Control
                type="text"
                name="name"
                value={values.name}
                onChange={handleChange}
                isValid={touched.name && !errors.name}
              />
              <Form.Control.Feedback type="invalid" style={{display:'block'}}>{errors.name}</Form.Control.Feedback>
            </Form.Group>
          </Form.Row>
          <Form.Row>
            <Form.Group as={Col} md="4" controlId="validationFormik02">
              <Form.Label>Email address</Form.Label>
              <Form.Control
                type="email"
                name="email"
                value={values.email}
                onChange={handleChange}
                isValid={touched.email && !errors.email}
              />
              <Form.Control.Feedback type="invalid" style={{display:'block'}}>{errors.email}</Form.Control.Feedback>
            </Form.Group>
          </Form.Row>
          <Form.Row>
            <Form.Group as={Col} md="4" controlId="validationFormik03">
              <Form.Label>Subject</Form.Label>
              <Form.Control
                type="text"
                name="subject"
                value={values.subject}
                onChange={handleChange}
                isValid={touched.subject && !errors.subject}
              />
              <Form.Control.Feedback type="invalid" style={{display:'block'}}>{errors.subject}</Form.Control.Feedback>
            </Form.Group>
          </Form.Row>
          <Form.Row>
            <Form.Group as={Col} md="4" controlId="validationFormik04">
              <Form.Label>Your message</Form.Label>
              <Form.Control
                style={{height:'15rem', width:'40rem'}}
                as="textarea"
                name="content"
                value={values.content}
                onChange={handleChange}
                isValid={touched.content && !errors.content}
              />
              <Form.Control.Feedback type="invalid" style={{display:'block'}}>{errors.content}</Form.Control.Feedback>
            </Form.Group>
          </Form.Row>
          <Button type="submit">Submit feedback</Button>
        </Form>
      )}
    </Formik>
  </div>
);

export default Feedback;