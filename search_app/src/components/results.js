import React from 'react'
import { Provider } from 'redux-bundler-react'
import { resultList as SorghumList } from 'sorghum-search'
// import { resultList as GrameneList } from 'gramene-search'

export default (store) => (
  <Provider store={store}>
    <div>
      <SorghumList />
      {/*<GrameneList />*/}
    </div>
  </Provider>
)
