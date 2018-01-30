import AddNewCell from './notebook';
import ReactDOM from 'react-dom';
import React from 'react';

const showAddNewButton = (element, url) => {
	ReactDOM.render(<AddNewCell url={url} />, element);
};

module.exports = showAddNewButton;

