
import React from 'react';

export default class AddNewCell extends React.Component {

	constructor(props) {
		//
		// constructor function
		// anything passed into object constructor is captured into "props"
		//
		super(props)
		// can define state variables as needed	
	};

	render() {
		// can't use "class" in HTML tags in .jsx; instead use "className" here
		// which will render to "class" in the output HTML
		return (
			<a className="add-circle" href={this.props.url}>Add New Cell</a>
		);
	};
	
};