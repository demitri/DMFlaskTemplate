import React from 'react'
import { Provider } from 'redux-bundler-react'
import { resultSummary as SorghumSummary } from 'sorghum-search'
// import { resultSummary as GrameneSummary } from 'gramene-search'

export default (store) => (
  <Provider store={store}>
    <ul className="list-unstyled category">
      <SorghumSummary />
      {/*<GrameneSummary />*/}
    </ul>
  </Provider>
)
