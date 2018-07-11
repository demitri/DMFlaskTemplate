import { h } from 'preact'
import { Provider } from 'redux-bundler-preact'

export default (store) => {
  const query = store.selectQueryObject();
  return (
    <Provider store={store}>
      <input type="search"
             class="form-control"
             value={query.q}
             placeholder="search here"
             onChange={e => {store.doUpdateTheQueries(`q=${e.target.value}`)}}
      />
    </Provider>
  )
}
