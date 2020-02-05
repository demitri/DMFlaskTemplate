import React from 'react'
import { Provider } from 'redux-bundler-react'
import { Status, Filters, Results, Views } from 'gramene-search'

export default (store) => (
  <Provider store={store}>
    <div className="row">
      <div className="col-md-2">
        <Status/>
        <Filters/>
        <Views/>
      </div>
      <div className="col-md-10">
        <Results/>
      </div>
    </div>
  </Provider>
)
