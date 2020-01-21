import React from 'react'
import {Provider, connect} from 'redux-bundler-react'
import {DebounceInput} from 'react-debounce-input'
import { Tabs, Nav, Tab, Row, Col } from 'react-bootstrap'
import { suggestions as SorghumSummary } from 'sorghum-search'
import { suggestions as GrameneSummary } from 'gramene-search'

const handleKey = (key, props) => {
  if (key === "Escape") {
    props.doClearSuggestions();
  }
  if (key === "Enter") {
    if (props.suggestionsTab === "sorghumbase") {
      props.doAcceptSorghumSuggestion(`q=${props.suggestionsQuery}`)
    }
  }
};

const SearchBarCmp = props =>
    <DebounceInput
        minLength={0}
        debounceTimeout={300}
        onChange={e => props.doChangeSuggestionsQuery(e.target.value)}
        onKeyUp={e => handleKey(e.key,props)}
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
  SearchBarCmp
);

const ResultsCmp = props => { //}({suggestionsQuery, suggestionsTab, doChangeSuggestionsTab}) => {
  if (props.suggestionsQuery) {
    const spinner = <img src="/static/images/dna_spinner.svg"/>;

    let genesStatus = props.grameneSuggestionsStatus === 'loading' ? spinner : props.grameneSuggestionsStatus;
    let siteStatus = props.sorghumSuggestionsStatus === 'loading' ? spinner : props.sorghumSuggestionsStatus;
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
        {/*<Tabs id="controlled-search-tabs" activeKey={props.suggestionsTab} onSelect={k => props.doChangeSuggestionsTab(k)}>*/}
        {/*  <Tab eventKey="gramene" title={`Genes ${genesStatus}`}>*/}
        {/*    <GrameneSummary/>*/}
        {/*  </Tab>*/}
        {/*  <Tab eventKey="sorghumbase" title={`Website ${siteStatus}`}>*/}
        {/*    <SorghumSummary/>*/}
        {/*  </Tab>*/}
        {/*  <Tab eventKey="germplasm" title="Germplasm" disabled>*/}
        {/*    <p>placeholder</p>*/}
        {/*  </Tab>*/}
        {/*</Tabs>*/}
      </div>
    );
  }
  return null;
}

const Results = connect(
  'selectSuggestionsQuery',
  'selectSuggestionsTab',
  'selectGrameneSuggestionsStatus',
  'selectSorghumSuggestionsStatus',
  'doChangeSuggestionsTab',
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

