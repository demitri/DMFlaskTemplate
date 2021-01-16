import React from 'react'
import {Provider, connect} from 'redux-bundler-react'
import {DebounceInput} from 'react-debounce-input'

const SearchBoxCmp = ({queryObject, doUpdateTheQueries}) =>
    <DebounceInput
        minLength={0}
        debounceTimeout={300}
        onChange={e => doUpdateTheQueries(`q=${e.target.value}`)}
        className="form-control"
        value={queryObject ? queryObject.q : ''}
        placeholder="search here"
    />;

const SearchBox = connect(
    'selectQueryObject',
    'doUpdateTheQueries',
    SearchBoxCmp
);

const Sbox = (store) => {
    return (
        <Provider store={store}>
            <SearchBox/>
        </Provider>
    )
};

export default Sbox;

