import React from 'react'
import { Provider } from 'redux-bundler-react'
import { Status, Filters, Results, Views } from '../../gramene-search/components/geneSearchUI'

const GrameneSearch = (store) => (
  <Provider store={store}>
    <div className="row no-margin no-padding">
      <div className="col-md-2 no-padding">
        <Status/>
        <Filters/>
        {/*<Views/>*/}
      </div>
      <div className="col-md-10 no-padding">
        <Results/>
      </div>
    </div>
  </Provider>
);

export default GrameneSearch;
