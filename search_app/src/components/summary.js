import React from 'react'
import { Provider } from 'redux-bundler-react'
import SorghumSummary from '../../sorghum-search/resultSummary'
// import { resultSummary as GrameneSummary } from 'gramene-search'

const Summary = (store) => (
  <Provider store={store}>
    <ul className="list-unstyled category">
      <SorghumSummary />
      {/*<GrameneSummary />*/}
    </ul>
  </Provider>
);

export default Summary;