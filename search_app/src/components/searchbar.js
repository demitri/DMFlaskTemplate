import React from 'react'
import { Provider, connect } from 'redux-bundler-react'
import { DebounceInput } from 'react-debounce-input'
import { Nav, Tab, Row, Col } from 'react-bootstrap'
import { suggestions as SorghumSummary } from 'sorghum-search'
import { suggestions as GrameneSummary } from 'gramene-search'

const handleKey = (e, props) => {
  if (e.key === "Escape") {
    props.doClearSuggestions();
  }
  if (e.key === "Enter") {
    if (props.suggestionsTab === "sorghumbase") {
      props.doAcceptSorghumSuggestion(`q=${props.suggestionsQuery}`)
    }
  }
  if (e.key === "Tab") {
    if (props.suggestionsTab === "gramene" && props.grameneSuggestionsReady) {
      e.preventDefault();
      document.getElementById('0-0').focus();
    }
  }
};

const SearchBarCmp = props =>
    <DebounceInput
        minLength={0}
        debounceTimeout={300}
        onChange={e => props.doChangeSuggestionsQuery(e.target.value)}
        onKeyDown={e => handleKey(e, props)}
        // onKeyUp={e => handleKey(e.key,props)}
        className="form-control"
        value={props.suggestionsQuery || ''}
        placeholder="Search Sorghumbase"
        id="sorghumbase-search-input"
        autoComplete="off"
        spellCheck="false"
    />;

const SearchBar = connect(
  'selectSuggestionsQuery',
  'selectSuggestionsTab',
  'doChangeSuggestionsQuery',
  'doClearSuggestions',
  'doAcceptSorghumSuggestion',
  'selectGrameneSuggestionsReady',
  SearchBarCmp
);

const ResultsCmp = props => {
  if (props.suggestionsQuery) {
    const spinner = <img src="/static/images/dna_spinner.svg"/>;

    let genesStatus = props.grameneSuggestionsStatus === 'loading' ? spinner : props.grameneSuggestionsStatus;
    let siteStatus = props.sorghumSuggestionsStatus === 'loading' ? spinner :
      <button onClick={e=>props.doAcceptSorghumSuggestion(`q=${props.suggestionsQuery}`)}>
        {props.sorghumSuggestionsStatus}
      </button>;
    return (
      <div className="search-suggestions">
        <Tab.Container id="controlled-search-tabs" activeKey={props.suggestionsTab} onSelect={k => props.doChangeSuggestionsTab(k)}>
          <Row>
            <Col>
              <Nav variant="tabs">
                <Nav.Item>
                  <Nav.Link eventKey="gramene">
                    <div className="suggestions-tab">Genes {genesStatus}</div>
                  </Nav.Link>
                </Nav.Item>
                <Nav.Item>
                  <Nav.Link eventKey="sorghumbase">
                    <div className="suggestions-tab">Website {siteStatus}</div>
                  </Nav.Link>
                </Nav.Item>
                <Nav.Item>
                  <Nav.Link eventKey="germplasm" disabled>
                    <div className="suggestions-tab">Germplasm</div>
                  </Nav.Link>
                </Nav.Item>
              </Nav>
            </Col>
          </Row>
          <Row>
            <Col>
              <Tab.Content>
                <Tab.Pane eventKey="gramene">
                  <GrameneSummary/>
                </Tab.Pane>
                <Tab.Pane eventKey="sorghumbase">
                  {/*<SorghumSummary/>*/}
                </Tab.Pane>
                <Tab.Pane eventKey="germplasm">
                  <p>placeholder</p>
                </Tab.Pane>
              </Tab.Content>
            </Col>
          </Row>
        </Tab.Container>
      </div>
    );
  }
  return null;
};

const Results = connect(
  'selectSuggestionsQuery',
  'selectSuggestionsTab',
  'selectGrameneSuggestionsStatus',
  'selectSorghumSuggestionsStatus',
  'doChangeSuggestionsTab',
  'doAcceptSorghumSuggestion',
  ResultsCmp
);

export default (store) => {
    return (
        <Provider store={store}>
          <div>
            <SearchBar/>
            <Results/>
          </div>
        </Provider>
    )
}

