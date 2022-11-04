<?php

namespace app\models;

use Yii;

/**
 * This is the model class for table "veiculo".
 *
 * @property int $id
 * @property string $placa
 * @property string $data
 * @property string $imagem
 */
class Veiculo extends \yii\db\ActiveRecord
{
    /**
     * {@inheritdoc}
     */
    public static function tableName()
    {
        return 'veiculo';
    }

    /**
     * {@inheritdoc}
     */
    public function rules()
    {
        return [
            [['placa', 'data', 'imagem'], 'required'],
            [['placa', 'imagem'], 'string'],
            [['data'], 'safe'],
        ];
    }

    /**
     * {@inheritdoc}
     */
    public function attributeLabels()
    {
        return [
            'id' => 'ID',
            'placa' => 'Placa',
            'data' => 'Data',
            'imagem' => 'Imagem',
        ];
    }
}
