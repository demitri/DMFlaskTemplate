import React from 'react'
import { Provider } from 'redux-bundler-react'
import SorghumList from '../../sorghum-search/resultList'
// import { resultList as GrameneList } from 'gramene-search'

const suggestions = (store) => (
  <Provider store={store}>
    <div>
      <SorghumList />
      {/*<GrameneList />*/}
    </div>
  </Provider>
);

export default suggestions;
