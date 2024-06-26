import React from 'react';
import Layout from '../components/Layout';
import '../components/Style.css';
import { useNavigate } from 'react-router';

function NoteList() {

  // 데이터 전달 X 

  const navigate = useNavigate();

  return (
    <Layout>
      <div className='NotelistBox'>

        <div className='NoteList'>
          <p>날짜</p>
          <p>시간</p>
          <p>이름</p>
          <p>분위기점수</p>
          <p>다시보기</p>
        </div>
      </div>

    </Layout>
  );
}

export default NoteList;