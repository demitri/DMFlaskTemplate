import React from 'react'
import { Provider } from 'redux-bundler-react'
import { Filters, Results, Views } from 'gramene-search'

export default (store) => (
  <Provider store={store}>
    <div className="row">
      <div className="col-md-2">
        <Filters/>
      </div>
      <div className="col-md-8">
        <Results/>
      </div>
      <div className="col-md-2">
        <Views/>
      </div>
    </div>
  </Provider>
)
